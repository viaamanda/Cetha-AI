from app.ai.extraction_service import extract_financial_data

sample_ocr = """
INDOMARET

TELUR 30000
MINYAK 18000
SUSU 25000

TOTAL 73000
"""

result = extract_financial_data(sample_ocr)

print(result)