import json
import google.generativeai as genai
from app.core.config import settings
from app.ai.prompting import SYSTEM_PROMPT

if settings.GEMINI_API_KEY:
    genai.configure(api_key=settings.GEMINI_API_KEY)

def generate_financial_analytics(transactions_data: list) -> dict:
    if not transactions_data:
        return {
            "tren": "Belum ada data transaksi untuk dianalisis.",
            "dominasi_kategori": "Belum tersedia",
            "anomali": None
        }

    prompt = f"""
{SYSTEM_PROMPT}

Berikut adalah data historis transaksi UMKM:
{json.dumps(transactions_data, indent=2)}

Tugas:
1. Analisis tren pengeluaran saat ini dengan bahasa sederhana.
2. Temukan kategori mana yang mendominasi pengeluaran dan mengapa.
3. Temukan apakah ada anomali (misalnya pengeluaran terlalu besar/tidak biasa). Jika tidak ada, kembalikan null.

Keluarkan output HANYA dalam format JSON sesuai skema berikut:
{{
  "tren": "...",
  "dominasi_kategori": "...",
  "anomali": "..."
}}
"""
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt, generation_config={"response_mime_type": "application/json"})
        data = json.loads(response.text)
        return data
    except Exception as e:
        return {
            "tren": "Gagal menganalisis data.",
            "dominasi_kategori": "Tidak diketahui",
            "anomali": f"Error sistem: {str(e)}"
        }
