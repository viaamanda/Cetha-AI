print("PROGRAM DIMULAI")

from app.ai.ocr_service import extract_text_from_image
print("OCR MODULE BERHASIL")

from app.ai.extraction_service import extract_financial_data
print("EXTRACTION MODULE BERHASIL")

from app.ai.categorization import categorize_item
print("CATEGORIZATION MODULE BERHASIL")

from app.ai.smartinsight_service import (
    calculate_category_totals,
    get_highest_category,
    generate_trend_insight
)

print("SMART INSIGHT MODULE BERHASIL")

from app.ai.recommendation_service import generate_recommendation
print("RECOMMENDATION MODULE BERHASIL")


# PATH GAMBAR NOTA
image_path = r"C:\Users\LENOVO\cethaa ai\backend\bukti tf konsum final.jpg"


# ======================
# OCR
# ======================

print("MULAI OCR...")

ocr_result = extract_text_from_image(image_path)

print("OCR SELESAI")
print(ocr_result)


# ======================
# GEMINI EXTRACTION
# ======================

print("MULAI GEMINI...")

structured_data = extract_financial_data(ocr_result)

print("GEMINI SELESAI")
print(structured_data)


# ======================
# CATEGORIZATION
# ======================

print("MULAI CATEGORIZATION...")

transactions = []

items = structured_data.get("items", [])

for item in items:

    item_name = item.get("name", "")

    price = item.get("price", 0)

    category = categorize_item(item_name)

    transactions.append({
        "category": category,
        "amount": price
    })

print("HASIL CATEGORIZATION:")
print(transactions)


# ======================
# SMART INSIGHT
# ======================

print("MULAI SMART INSIGHT...")

totals = calculate_category_totals(transactions)

highest = get_highest_category(totals)

insight = generate_trend_insight(highest)

print("SMART INSIGHT:")
print(insight)


# ======================
# AI RECOMMENDATION
# ======================

print("MULAI AI RECOMMENDATION...")

recommendations = generate_recommendation(totals)

print("HASIL REKOMENDASI:")

for rec in recommendations:

    print("-", rec)