from fastapi import APIRouter
from pydantic import BaseModel
from app.ai.categorization import categorize_item

router = APIRouter()

class ItemInput(BaseModel):
    item_name: str

class BulkItemInput(BaseModel):
    items: list[str]

@router.post("/item")
async def kategorisasi_item(input: ItemInput):
    result = categorize_item(input.item_name)
    return {"status": "success", "item": input.item_name, "kategori": result}

@router.post("/bulk")
async def kategorisasi_bulk(input: BulkItemInput):
    results = [{"item": item, "kategori": categorize_item(item)} for item in input.items]
    return {"status": "success", "data": results}