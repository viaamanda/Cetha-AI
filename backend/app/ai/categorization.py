def categorize_item(item_name):

    item = item_name.lower()

    food_keywords = [
        "mie",
        "nasi",
        "kopi",
        "teh",
        "roti",
        "ayam"
    ]

    transport_keywords = [
        "bensin",
        "pertalite",
        "parkir",
        "grab",
        "gojek"
    ]

    health_keywords = [
        "obat",
        "vitamin"
    ]

    if any(word in item for word in food_keywords):
        return "Makanan"

    elif any(word in item for word in transport_keywords):
        return "Transportasi"

    elif any(word in item for word in health_keywords):
        return "Kesehatan"

    return "Lainnya"