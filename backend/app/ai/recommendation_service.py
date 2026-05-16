# app/ai/recommendation_service.py

# Threshold pengeluaran per kategori (dalam Rupiah)
THRESHOLDS = {
    "Bahan Baku": 500_000,
    "Operasional": 300_000,
    "Transportasi": 200_000,
    "Gaji": 1_000_000,
    "Pemasaran": 250_000,
    "Peralatan": 400_000,
}

TIPS = {
    "Bahan Baku": "Pengeluaran bahan baku cukup tinggi. Pertimbangkan membeli dalam jumlah besar (grosir) untuk menekan biaya.",
    "Operasional": "Biaya operasional besar. Cek apakah ada pengeluaran yang bisa dikurangi seperti listrik atau sewa.",
    "Transportasi": "Biaya transportasi cukup besar. Pertimbangkan mengoptimalkan rute pengiriman.",
    "Gaji": "Pengeluaran gaji tinggi. Pastikan produktivitas karyawan sebanding dengan biaya yang dikeluarkan.",
    "Pemasaran": "Biaya pemasaran cukup besar. Evaluasi channel mana yang paling efektif.",
    "Peralatan": "Pengeluaran peralatan tinggi. Pertimbangkan perawatan rutin agar peralatan lebih awet.",
}

def generate_recommendation(totals: dict) -> list:
    """Generate rekomendasi berdasarkan total pengeluaran per kategori."""
    if not totals:
        return ["Belum ada data transaksi untuk dianalisis."]

    recommendations = []

    for category, amount in totals.items():
        threshold = THRESHOLDS.get(category, 0)
        if threshold and amount > threshold:
            tip = TIPS.get(category)
            if tip:
                recommendations.append(tip)

    if not recommendations:
        recommendations.append(
            "Pengeluaran masih dalam batas wajar. Pertahankan pengelolaan keuanganmu!"
        )

    return recommendations