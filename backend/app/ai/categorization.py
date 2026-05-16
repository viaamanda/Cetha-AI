# app/ai/categorization.py
import json
import google.generativeai as genai
from app.core.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

# Kategori sesuai proposal Cetha AI
VALID_CATEGORIES = [
    "Bahan Baku",
    "Operasional", 
    "Transportasi",
    "Gaji",
    "Pemasaran",
    "Peralatan",
    "Lainnya"
]

def categorize_item(item_name: str) -> str:
    """Kategorisasi satu item menggunakan Gemini."""
    if not item_name.strip():
        return "Lainnya"

    prompt = f"""
    Kategorikan item belanja UMKM berikut ke salah satu kategori ini:
    {", ".join(VALID_CATEGORIES)}

    Item: "{item_name}"

    Kembalikan HANYA nama kategorinya saja, tanpa penjelasan.
    Contoh output: Bahan Baku
    """

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        result = response.text.strip()

        # Validasi output harus salah satu dari kategori yang valid
        if result in VALID_CATEGORIES:
            return result
        return "Lainnya"

    except Exception:
        return "Lainnya"