import logging
import os
import time

import psycopg


logger = logging.getLogger(__name__)


def get_database_url() -> str:
    host = os.getenv("POSTGRES_HOST", "localhost")
    port = os.getenv("POSTGRES_PORT", "5432")
    dbname = os.getenv("POSTGRES_DB", "rag")
    user = os.getenv("POSTGRES_USER", "rag")
    password = os.getenv("POSTGRES_PASSWORD", "rag")
    return f"postgresql://{user}:{password}@{host}:{port}/{dbname}"


def get_connection() -> psycopg.Connection:
    return psycopg.connect(get_database_url())


def initialize_database(max_retries: int = 10, retry_delay: int = 3) -> None:
    last_error: Exception | None = None

    for attempt in range(1, max_retries + 1):
        try:
            with get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")
                    cur.execute(
                        """
                        CREATE TABLE IF NOT EXISTS documents (
                            id SERIAL PRIMARY KEY,
                            title TEXT NOT NULL,
                            source_type TEXT NOT NULL,
                            created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
                        );
                        """
                    )
                    cur.execute(
                        """
                        CREATE TABLE IF NOT EXISTS chunks (
                            id SERIAL PRIMARY KEY,
                            document_id INTEGER NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
                            chunk_index INTEGER NOT NULL,
                            text TEXT NOT NULL,
                            embedding vector,
                            created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
                        );
                        """
                    )
                    cur.execute(
                        """
                        CREATE INDEX IF NOT EXISTS idx_chunks_document_id
                        ON chunks (document_id);
                        """
                    )
                conn.commit()
            logger.info("Database initialization completed")
            return
        except Exception as exc:
            last_error = exc
            logger.warning(
                "Database initialization failed (attempt %s/%s): %s",
                attempt,
                max_retries,
                exc,
            )
            time.sleep(retry_delay)

    raise RuntimeError("Failed to initialize database") from last_error


def check_database_connection() -> bool:
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1;")
                cur.fetchone()
        return True
    except Exception:
        return False
