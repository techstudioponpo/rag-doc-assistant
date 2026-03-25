# rag-doc-assistant

Next.js・FastAPI・pgvectorを使用した、ドキュメントベースの質問応答を行うRAGアプリケーションです。

## 概要

rag-doc-assistant は、ドキュメント（主にPDF）の内容をもとに質問に回答するRAG（Retrieval-Augmented Generation）アプリケーションです。

最小構成でRAGの仕組みを実装しつつ、将来的に以下のような用途へ拡張可能な設計としています。

* 社内マニュアル検索AI
* FAQ自動回答システム
* 問い合わせ一次対応AI
* ナレッジベース検索アプリ

---

## 特徴

* Next.js + TypeScript によるフロントエンド
* FastAPI によるバックエンドAPI
* PostgreSQL + pgvector によるベクトル検索
* OpenAI API による回答生成
* Docker Compose による再現可能な開発環境
* 拡張しやすいシンプルなRAG構成

---

## アーキテクチャ

* Frontend：Next.js + TypeScript
* Backend：FastAPI
* Database：PostgreSQL + pgvector
* AI：OpenAI API
* Runtime：Docker Compose

---

## 処理フロー

### 文書登録

1. PDFアップロード
2. テキスト抽出
3. チャンク分割
4. Embedding生成
5. データベース保存

### 質問応答

1. ユーザーが質問入力
2. 質問をEmbedding化
3. ベクトル検索（pgvector）
4. 関連テキスト取得
5. OpenAI APIへ送信
6. 回答生成
7. フロントへ表示

---

## 用語補足

* チャンク分割
  長い文章を検索しやすくするために、小さな単位（500〜1000文字程度）に分割する処理

* Embedding（エンベディング）
  文章を意味ベースで検索できるように、数値（ベクトル）に変換する処理

* ベクトル検索（pgvector）
  数値化された文章同士の「意味の近さ」をもとに、関連するテキストを検索する仕組み

---

## ディレクトリ構成

```
.
├─ frontend/
├─ backend/
├─ db/
├─ docs/
├─ docker-compose.yml
├─ .env.example
└─ README.md
```

---

## セットアップ

1. リポジトリ取得

   git clone https://github.com/techstudioponpo/rag-doc-assistant.git
   cd rag-doc-assistant

2. 環境変数設定

   cp .env.example .env

.env に以下を設定

```
OPENAI_API_KEY=your_api_key_here
POSTGRES_DB=rag
POSTGRES_USER=rag
POSTGRES_PASSWORD=rag
```

3. 起動

```
docker compose up
```

4. アクセス

```
http://localhost:3000
```

---

## 注意事項

* OpenAI APIキーが必要です
* APIキーはフロントエンドには公開されません
* 本リポジトリはポートフォリオ用途として公開しています

---

## 今後の拡張

* 複数ドキュメント対応
* 履歴管理
* UI改善
* 外部サービス連携

---

## ライセンス

本リポジトリはポートフォリオ目的で公開しています。
無断での利用・再配布は禁止します。
