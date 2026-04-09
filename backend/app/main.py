from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db import check_database_connection, initialize_database

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_event():
    initialize_database()


@app.get("/")
def read_root():
    return {"message": "backend is running"}


@app.get("/health")
def health_check():
    db_status = "ok" if check_database_connection() else "error"
    app_status = "ok" if db_status == "ok" else "degraded"
    return {"status": app_status, "database": db_status}
