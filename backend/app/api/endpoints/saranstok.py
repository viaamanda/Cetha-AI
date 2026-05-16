from fastapi import APIRouter
from pydantic import BaseModel
from app.ai.extraction_service import calculate_category_totals
from app.ai.recommendation_service import generate_recommendation

router = APIRouter()

class TransaksiList(BaseModel):
    transactions: list[dict]

@router.post("/")
async def get_saran_stok(input: TransaksiList):
    if not input.transactions:
        return {"status": "error", "message": "Belum ada data transaksi"}

    totals = calculate_category_totals(input.transactions)
    rekomendasi = generate_recommendation(totals)

    return {
        "status": "success",
        "data": {
            "category_totals": totals,
            "rekomendasi": rekomendasi
        }
    }