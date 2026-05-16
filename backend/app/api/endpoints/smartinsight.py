from fastapi import APIRouter
from pydantic import BaseModel
from app.ai.extraction_service import (
    calculate_category_totals,
    get_highest_category,
    generate_trend_insight
)

router = APIRouter()

class TransaksiList(BaseModel):
    transactions: list[dict]

@router.post("/")
async def get_insight(input: TransaksiList):
    if not input.transactions:
        return {"status": "error", "message": "Belum ada data transaksi"}

    totals = calculate_category_totals(input.transactions)
    highest = get_highest_category(totals)
    insight = generate_trend_insight(highest)

    return {
        "status": "success",
        "data": {
            "category_totals": totals,
            "highest_category": highest,
            "insight": insight
        }
    }