# Cetha AI Backend

Backend service for Cetha AI, a fintech solution for UMKM in Surabaya. Built with FastAPI, integrating Google Cloud Vision for OCR and Gemini for smart financial insights.

## Project Structure

```text
Cetha AI/
├── app/
│   ├── api/
│   │   └── endpoints/     # API route handlers
│   ├── core/              # Global config, security, constants
│   ├── models/            # Pydantic & DB models (future)
│   ├── services/          # Business logic (OCR, AI, etc.)
│   └── main.py            # FastAPI entry point
├── requirements.txt       # Dependencies
├── .env                   # Environment variables
└── README.md
```

## Setup

1. **Create Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**
   - Rename `.env.example` to `.env` (if applicable) or update existing `.env`.
   - Add your `GEMINI_API_KEY`.
   - Place `gcp-credentials.json` and `firebase-credentials.json` in the root directory.

4. **Run the Server:**
   ```bash
   uvicorn app.main:app --reload
   ```

## API Documentation

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
- Health Check: `http://localhost:8000/health`
