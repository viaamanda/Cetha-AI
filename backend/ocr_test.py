from app.ai.ocr_service import extract_text_from_image
import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "percobaan nota 1.jpeg")

print(f"Checking for image at: {image_path}")
if not os.path.exists(image_path):
    print("Error: Image file not found!")
else:
    try:
        result = extract_text_from_image(image_path)
        print("OCR Result:")
        print("-" * 20)
        print(result)
        print("-" * 20)
    except Exception as e:
        print(f"Error during OCR: {e}")