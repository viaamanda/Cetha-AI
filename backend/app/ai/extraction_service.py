import os
import sys
import json
import warnings
from pathlib import Path

# Suppress the deprecation warning from google-generativeai to avoid user confusion
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai

# Add the project root to sys.path so 'app' can be found
current_file = Path(__file__).resolve()
# extraction_service.py is in backend/app/ai/
# We want to add 'backend' to sys.path
project_root = current_file.parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

try:
    from app.core.config import settings
except (ImportError, ModuleNotFoundError):
    # Fallback if not running as part of the 'app' package
    sys.path.append(str(current_file.parent.parent))
    from core.config import settings

# Configure Gemini
# ✅ Ambil dari settings saja
api_key = settings.GEMINI_API_KEY
if not api_key:
    raise ValueError("GEMINI_API_KEY belum diset di file .env")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

def extract_financial_data(ocr_text):
    """Extract financial transaction data from OCR text using Gemini."""
    prompt = f"""
    Extract financial transaction data from this receipt text.
    Return ONLY valid JSON.

    OCR TEXT:
    {ocr_text}

    Format:
    {{
        "store_name": "",
        "items": [
            {{
                "name": "",
                "price": 0,
                "category": ""
            }}
        ],
        "total": 0
    }}
    """

    response = model.generate_content(prompt)
    
    if not response or not response.text:
        raise Exception("Failed to get response from Gemini")
        
    # Clean response text
    cleaned_text = response.text
    if "```json" in cleaned_text:
        cleaned_text = cleaned_text.split("```json")[1].split("```")[0].strip()
    elif "```" in cleaned_text:
        cleaned_text = cleaned_text.split("```")[1].split("```")[0].strip()
    else:
        cleaned_text = cleaned_text.strip()
        
    return json.loads(cleaned_text)

def categorize_expenses(structured_data):
    """Categorize items in the structured data."""
    prompt = f"""
    Categorize each item in this JSON data into common expense categories (e.g., Food, Transport, Utilities, etc.).
    Return ONLY the updated JSON.

    JSON_INPUT:
    {json.dumps(structured_data, indent=2)}
    """
    
    response = model.generate_content(prompt)
    
    if not response or not response.text:
        return structured_data
        
    text = response.text
    if "```json" in text:
        text = text.split("```json")[1].split("```")[0].strip()
    elif "```" in text:
        text = text.split("```")[1].split("```")[0].strip()
    else:
        text = text.strip()
        
    try:
        return json.loads(text)
    except:
        return structured_data

if __name__ == "__main__":
    # Test text
    sample_ocr = """
    TOKO MAJU JAYA
    Jl. Merdeka No. 10
    
    1. Kopi Susu      15.000
    2. Roti Bakar     20.000
    ------------------------
    TOTAL             35.000
    """
    
    print("Testing extraction service...")
    try:
        data = extract_financial_data(sample_ocr)
        print("\nExtracted Data:")
        print(json.dumps(data, indent=2))
        
        categorized = categorize_expenses(data)
        print("\nCategorized Data:")
        print(json.dumps(categorized, indent=2))
    except Exception as e:
        print(f"Error during test: {e}")

from collections import defaultdict

def calculate_category_totals(transactions: list) -> dict:
    """Hitung total pengeluaran per kategori dari list transaksi."""
    totals = defaultdict(int)
    for trx in transactions:
        category = trx.get("category", "Lainnya")
        amount = trx.get("amount", 0)
        totals[category] += amount
    return dict(totals)

def get_highest_category(totals: dict) -> dict:
    """Ambil kategori dengan pengeluaran tertinggi."""
    if not totals:
        return {"category": "-", "amount": 0}
    highest = max(totals, key=totals.get)
    return {"category": highest, "amount": totals[highest]}

def generate_trend_insight(highest: dict) -> str:
    """Generate kalimat insight dari kategori tertinggi."""
    category = highest["category"]
    amount = highest["amount"]
    return f"Kategori pengeluaran terbesar adalah {category} dengan total Rp {amount:,}"