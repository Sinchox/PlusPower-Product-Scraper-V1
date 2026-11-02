# PlusPower Product Scraper

Single-folder project scaffold. Every project file is kept in this directory; there are no nested folders.

## Stack
- React + TypeScript frontend
- FastAPI backend
- Supabase Postgres (optional until credentials are configured)
- Tavily search fallback
- CSV export

## Run the backend
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
cp .env.example .env
uvicorn api:app --reload
```

## Run the frontend
```bash
npm install
npm run dev
```

The frontend expects the API at `http://localhost:8000`. Set `VITE_API_URL` if needed.

## Safety and scraping behaviour
The scraper identifies Cloudflare/challenge pages and HTTP 429 responses, then stops rather than attempting CAPTCHA bypass, stealth, or proxy rotation. Missing product fields remain null. Tavily is a discovery/verification fallback, not a source for inventing product data.

This is a starter implementation. Configure credentials and validate selectors against current PlusPower pages before production use.
