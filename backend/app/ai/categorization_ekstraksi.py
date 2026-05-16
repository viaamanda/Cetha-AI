import json
import google.generativeai as genai
from app.core.config import settings
from app.ai.prompting import SYSTEM_PROMPT

# Configure Gemini API
if settings.GEMINI_API_KEY:
    genai.configure(api_key=settings.GEMINI_API_KEY)

def categorize_and_validate_receipt(ocr_text: str) -> dict:
    if not ocr_text.strip():
        return {
            "tanggal": None,
            "total_harga": 0.0,
            "kategori": "Tidak Diketahui",
            "items": [],
            "perlu_verifikasi": True,
            "alasan_verifikasi": "Teks OCR kosong atau gambar nota tidak terbaca sama sekali."
        }

    prompt = f"""
{SYSTEM_PROMPT}

Berikut adalah teks hasil scan OCR dari sebuah struk/nota pembelian:
{ocr_text}

Tugas:
1. Ekstrak informasi transaksi dari teks di atas (tanggal, item, harga, dll).
2. Jika tanggal atau total harga tidak ada, atau hasil OCR terlihat berantakan/buram, atur 'perlu_verifikasi': true dan jelaskan alasannya.
3. Kategorikan transaksi ke dalam: Bahan Baku, Operasional, Gaji, Pemasaran, Peralatan, atau Lainnya.
4. Jangan halusinasi data. Jika tidak ada harga spesifik, biarkan total sesuai apa yang bisa dibaca dan nyalakan verifikasi.

Keluarkan hasil HANYA dalam format JSON sesuai skema berikut:
{{
  "tanggal": "YYYY-MM-DD",
  "total_harga": 100000.0,
  "kategori": "Nama Kategori",
  "items": [
    {{"nama_item": "...", "harga": 0.0, "jumlah": 1, "total": 0.0}}
  ],
  "perlu_verifikasi": false,
  "alasan_verifikasi": null
}}
"""
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt, generation_config={"response_mime_type": "application/json"})
        data = json.loads(response.text)
        return data
    except Exception as e:
        return {
            "tanggal": None,
            "total_harga": 0.0,
            "kategori": "Tidak Diketahui",
            "items": [],
            "perlu_verifikasi": True,
            "alasan_verifikasi": f"Terjadi kesalahan sistem saat memproses AI: {str(e)}"
        }
