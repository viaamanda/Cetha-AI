def generate_recommendation(totals):

    recommendations = []

    food_total = totals.get("Makanan", 0)

    transport_total = totals.get("Transportasi", 0)

    health_total = totals.get("Kesehatan", 0)

    # REKOMENDASI MAKANAN
    if food_total > 50000:

        recommendations.append(
            "Pengeluaran makanan cukup tinggi. "
            "Cobalah mengurangi pembelian makanan di luar."
        )

    # REKOMENDASI TRANSPORTASI
    if transport_total > 30000:

        recommendations.append(
            "Biaya transportasi cukup besar. "
            "Pertimbangkan menggunakan transportasi umum."
        )

    # REKOMENDASI KESEHATAN
    if health_total > 20000:

        recommendations.append(
            "Pengeluaran kesehatan meningkat. "
            "Pastikan menjaga pola hidup sehat."
        )

    # DEFAULT
    if len(recommendations) == 0:

        recommendations.append(
            "Pengeluaran masih cukup stabil. "
            "Pertahankan pengelolaan keuanganmu!"
        )

    return recommendations