from typing import Any
from config import SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY
try:
    from supabase import create_client
except Exception:
    create_client = None
_client = None
if create_client and SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY:
    _client = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)

def list_products() -> list[dict[str, Any]]:
    if not _client: return []
    return _client.table("products").select("*").order("created_at", desc=True).execute().data

def save_product(product: dict[str, Any]) -> dict[str, Any]:
    if not _client: raise RuntimeError("Supabase is not configured")
    result = _client.table("products").upsert(product, on_conflict="url").execute()
    return result.data[0] if result.data else product
