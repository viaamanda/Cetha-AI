from fastapi import APIRouter, UploadFile, File
import shutil, os, tempfile
from app.ai.ocr_service import extract_text_from_image
from app.ai.extraction_service import extract_financial_data, categorize_expenses

router = APIRouter()

@router.post("/scan")
async def scan_nota(file: UploadFile = File(...)):
    # Simpan file sementara karena Tesseract butuh path file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        shutil.copyfileobj(file.file, tmp)
        tmp_path = tmp.name

    try:
        # Step 1: OCR
        ocr_text = extract_text_from_image(tmp_path)
        # Step 2: Ekstraksi data via Gemini
        extracted = extract_financial_data(ocr_text)
        # Step 3: Kategorisasi
        categorized = categorize_expenses(extracted)
    finally:
        os.unlink(tmp_path)

    return {
        "status": "success",
        "ocr_text": ocr_text,
        "data": categorized
    }