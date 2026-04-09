"use client";

import { useState } from "react";

const apiBaseUrl =
  process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000";

export default function Home() {
  const [result, setResult] = useState("未確認");
  const [loading, setLoading] = useState(false);

  const handleClick = async () => {
    setLoading(true);

    try {
      const res = await fetch(`${apiBaseUrl}/health`);
      const data = await res.json();

      setResult(JSON.stringify(data));
    } catch (e) {
      console.error(e);
      setResult("エラー");
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="flex min-h-screen items-center justify-center bg-slate-50 px-4">
      <div className="space-y-4 rounded-2xl border border-slate-200 bg-white p-8 shadow-md">
        <h1 className="text-xl font-bold text-slate-900">RAG Frontend</h1>

        <button
          onClick={handleClick}
          disabled={loading}
          className="rounded-full bg-blue-600 px-5 py-3 font-semibold text-white shadow-lg shadow-blue-600/30 transition-all duration-150 hover:-translate-y-0.5 hover:bg-blue-500 hover:shadow-xl hover:shadow-blue-600/40 active:translate-y-0.5 active:scale-[0.98] active:bg-blue-700 disabled:cursor-not-allowed disabled:opacity-70"
        >
          {loading ? "確認中..." : "バックエンドを確認"}
        </button>

        <div className="text-sm text-slate-700">
          <strong>Result:</strong> {result}
        </div>
      </div>
    </main>
  );
}
