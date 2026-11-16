
from library_item import Book, Magazine
from library import Library


def main():
    """Menjalankan sistem manajemen perpustakaan."""

    perpustakaan = Library()

    # Menambahkan beberapa buku
    buku1 = Book("B001", "Pemrograman Python", "Budi Santoso")
    buku2 = Book("B002", "Belajar OOP Python", "Andi Wijaya")

    # Menambahkan beberapa majalah
    majalah1 = Magazine("M001", "Teknologi Masa Kini", "Edisi 12")
    majalah2 = Magazine("M002", "Dunia Komputer", "Edisi 25")

    print("=== SISTEM MANAJEMEN PERPUSTAKAAN ===")

    perpustakaan.tambah_item(buku1)
    perpustakaan.tambah_item(buku2)
    perpustakaan.tambah_item(majalah1)
    perpustakaan.tambah_item(majalah2)

    # Menampilkan katalog
    perpustakaan.tampilkan_katalog()

    # Mencari item berdasarkan judul
    perpustakaan.cari_item("Python")

    # Mencari item berdasarkan ID
    perpustakaan.cari_item("M001")

    # Demonstrasi status peminjaman
    print("\n=== STATUS PEMINJAMAN ===")
    buku1.pinjam()
    print(buku1.get_detail())

    print("\n=== KATALOG SETELAH PEMINJAMAN ===")
    perpustakaan.tampilkan_katalog()

    # Demonstrasi pengembalian
    buku1.kembalikan()
    print("\nBuku berhasil dikembalikan.")

    print("\n=== KATALOG SETELAH PENGEMBALIAN ===")
    perpustakaan.tampilkan_katalog()

    # Demonstrasi polymorphism pada perhitungan denda
    print("\n=== PERHITUNGAN DENDA ===")
    print(f"Denda buku: Rp{buku1.hitung_denda(3):,}")
    print(f"Denda majalah: Rp{majalah1.hitung_denda(3):,}")


if __name__ == "__main__":
    main()
