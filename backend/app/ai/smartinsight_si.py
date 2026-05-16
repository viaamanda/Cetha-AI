from collections import defaultdict

def calculate_category_totals(transactions):

    totals = defaultdict(int)

    for trx in transactions:

        category = trx["category"]

        amount = trx["amount"]

        totals[category] += amount

    return dict(totals)


def get_highest_category(totals):

    highest = max(totals, key=totals.get)

    return {
        "category": highest,
        "amount": totals[highest]
    }


def generate_trend_insight(highest):

    category = highest["category"]

    amount = highest["amount"]

    return f"""
Kategori pengeluaran terbesar adalah {category}
dengan total Rp {amount:,}
"""