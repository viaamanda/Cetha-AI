# app/ai/ocr_service.py
import pytesseract
from PIL import Image, ImageFilter, ImageEnhance
import os

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

def preprocess_image(image: Image.Image) -> Image.Image:
    """Tingkatkan kualitas gambar sebelum OCR."""
    # Konversi ke grayscale
    image = image.convert("L")
    # Tingkatkan kontras
    image = ImageEnhance.Contrast(image).enhance(2.0)
    # Sharpen
    image = image.filter(ImageFilter.SHARPEN)
    return image

def extract_text_from_image(image_path: str) -> str:
    """Extract text dari gambar menggunakan Tesseract OCR."""
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"File tidak ditemukan: {image_path}")

    image = Image.open(image_path)
    image = preprocess_image(image)

    # lang="ind" untuk Bahasa Indonesia
    text = pytesseract.image_to_string(image, lang="ind+eng")

    if not text.strip():
        raise ValueError("OCR tidak berhasil mengekstrak teks dari gambar.")

    return text