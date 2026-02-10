# Customer Support Bot with Memory

Professional, concise README for the Agentic Customer Support Bot that
demonstrates selective context injection and persistent semantic memory.

## Summary

This project implements a CLI-based customer support assistant that uses
Azure OpenAI models to (1) embed user queries, (2) store and retrieve
relevant past issues via a local vector store, and (3) generate context-aware
responses while updating memory for future recalls.

## Key Features

- Persistent local vector memory for past customer issues
- Semantic retrieval with cosine similarity (top-k selection)
- Selective prompt injection to avoid token bloat
- Uses Azure OpenAI for embeddings and chat completions

## Models

- Embeddings: text-embedding-3-small
- Chat: gpt-5.2-chat

## Quick Start

1. Create and activate a virtual environment (recommended).

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

2. Populate the `.env` file with your Azure OpenAI settings. At minimum set:

- `AZURE_OPENAI_API_KEY`
- `AZURE_OPENAI_ENDPOINT`
- `EMBEDDING_DEPLOYMENT` (e.g. text-embedding-3-small)
- `CHAT_DEPLOYMENT` (e.g. gpt-5.2-chat)

3. Run the app from the project root:

```bash
python app.py
```

## How It Works (high level)

1. User enters a query via the CLI.
2. Query is embedded and compared against stored embeddings.
3. Top-k relevant past issues are retrieved (cosine similarity).
4. Relevant issues are injected into the prompt sent to the chat model.
5. Response is returned and the new issue is stored back into the vector memory.

## Files of Interest

- `app.py` — CLI entrypoint and request routing
- `agent.py` — Orchestration: memory retrieval, prompt construction, responses
- `memory_vector.py` — Embedding generation, vector store, similarity search
- `azure_openai_client.py` — Azure OpenAI wrapper for embeddings and chat

## Troubleshooting

- Ensure environment variables in `.env` are correct.
- Verify model deployment names match your Azure OpenAI resource.

## Contribution

Feel free to open issues or submit PRs for improvements (documentation,
CLI niceties, or memory storage alternatives).

---

Updated to a professional, concise format. See the file at
[customer_agentic_support_bot/README.md](customer_agentic_support_bot/README.md) for details.
