from pydantic import BaseModel, Field
from typing import List, Optional

SYSTEM_PROMPT = """
Kamu adalah Cetha AI, asisten keuangan cerdas yang membantu pelaku Usaha Mikro, Kecil, dan Menengah (UMKM) di Surabaya.
Tugas kamu adalah menganalisis data keuangan, mengkategorikan transaksi, memberikan insight, dan rekomendasi bisnis.
Gunakan Bahasa Indonesia yang sederhana, jelas, dan mudah dipahami oleh pelaku UMKM. Jangan gunakan jargon akuntansi yang rumit.

Prinsip utama:
1. Selalu berikan output dalam format JSON terstruktur yang valid.
2. Jika data tidak lengkap, tidak jelas, atau mencurigakan, atur "perlu_verifikasi": true dan jelaskan alasannya di "alasan_verifikasi".
3. Jangan pernah mengarang/halusinasi data.
4. Prioritaskan akurasi.
"""

class ItemTransaksi(BaseModel):
    nama_item: str = Field(description="Nama barang atau jasa")
    harga: float = Field(description="Harga satuan item")
    jumlah: int = Field(default=1, description="Jumlah item")
    total: float = Field(description="Total harga untuk item ini")

class ValidasiTransaksi(BaseModel):
    tanggal: Optional[str] = Field(description="Tanggal transaksi (YYYY-MM-DD), null jika tidak ditemukan", default=None)
    total_harga: float = Field(description="Total harga keseluruhan dalam struk/nota")
    kategori: str = Field(description="Kategori pengeluaran UMKM (Bahan Baku, Operasional, Gaji, Pemasaran, Peralatan, Lainnya)")
    items: List[ItemTransaksi] = Field(description="Daftar item dalam transaksi")
    perlu_verifikasi: bool = Field(description="True jika data tidak lengkap, buram, atau meragukan")
    alasan_verifikasi: Optional[str] = Field(description="Alasan mengapa data perlu diverifikasi secara manual oleh user", default=None)

class InsightKeuangan(BaseModel):
    tren: str = Field(description="Penjelasan tren pengeluaran saat ini dengan bahasa sederhana")
    dominasi_kategori: str = Field(description="Kategori pengeluaran terbesar beserta alasannya")
    anomali: Optional[str] = Field(description="Apakah ada pengeluaran yang tidak wajar? Berikan null jika tidak ada", default=None)

class RekomendasiBisnis(BaseModel):
    rekomendasi_stok: List[str] = Field(description="Saran penyediaan stok barang (misal: musiman atau yang cepat habis)")
    strategi_keuangan: List[str] = Field(description="Saran strategi keuangan praktis untuk menghemat biaya atau menaikkan profit")
