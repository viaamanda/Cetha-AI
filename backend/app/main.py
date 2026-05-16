from fastapi import FastAPI, UploadFile, File
import shutil
import os

from app.ai.ocr_service import extract_text_from_image
from app.ai.extraction_service import extract_financial_data
from app.ai.categorization import categorize_item

from app.ai.smartinsight_service import (
    calculate_category_totals,
    get_highest_category,
    generate_trend_insight
)

from app.ai.recommendation_service import generate_recommendation

app = FastAPI()


@app.post("/analyze-receipt")
async def analyze_receipt(file: UploadFile = File(...)):

    try:

        upload_path = f"temp_{file.filename}"

        with open(upload_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        print("FILE BERHASIL DISIMPAN")

        ocr_result = extract_text_from_image(upload_path)

        print("OCR BERHASIL")

        structured_data = extract_financial_data(ocr_result)

        print("EXTRACTION BERHASIL")
        print(structured_data)

        transactions = []

        items = structured_data.get("items", [])

        for item in items:

            item_name = item.get("name", "")

            price = item.get("price", 0)

            category = categorize_item(item_name)

            transactions.append({
                "name": item_name,
                "category": category,
                "amount": price
            })

        totals = calculate_category_totals(transactions)

        highest = get_highest_category(totals)

        insight = generate_trend_insight(highest)

        recommendations = generate_recommendation(totals)

        os.remove(upload_path)

        return {
            "transactions": transactions,
            "totals": totals,
            "insight": insight,
            "recommendations": recommendations
        }

    except Exception as e:

        return {
            "error": str(e)
        }