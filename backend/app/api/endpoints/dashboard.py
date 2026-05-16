from fastapi import APIRouter
from pydantic import BaseModel
from app.ai.extraction_service import calculate_category_totals, get_highest_category

router = APIRouter()

class DashboardInput(BaseModel):
    transactions: list[dict]

@router.post("/")
async def get_dashboard(input: DashboardInput):
    if not input.transactions:
        return {"status": "success", "data": {
            "total_pengeluaran": 0,
            "distribusi_kategori": {},
            "kategori_tertinggi": None,
            "jumlah_transaksi": 0
        }}

    totals = calculate_category_totals(input.transactions)
    highest = get_highest_category(totals)
    total = sum(totals.values())

    distribusi = {
        k: {"total": v, "persentase": round(v / total * 100, 1)}
        for k, v in totals.items()
    }

    return {
        "status": "success",
        "data": {
            "total_pengeluaran": total,
            "distribusi_kategori": distribusi,
            "kategori_tertinggi": highest,
            "jumlah_transaksi": len(input.transactions)
        }
    }