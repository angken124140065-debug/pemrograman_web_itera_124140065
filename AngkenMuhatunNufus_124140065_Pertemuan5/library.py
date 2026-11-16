
class Library:
    """Class untuk mengelola koleksi item perpustakaan."""

    def __init__(self):
        self.__koleksi = []

    def tambah_item(self, item):
        """Menambahkan item baru ke koleksi perpustakaan."""
        for data in self.__koleksi:
            if data._id == item._id:
                print("ID item sudah digunakan!")
                return

        self.__koleksi.append(item)
        print(f"Item '{item.judul}' berhasil ditambahkan.")

    def tampilkan_katalog(self):
        """Menampilkan semua item yang tersedia."""
        print("\n=== KATALOG PERPUSTAKAAN ===")

        item_tersedia = [
            item for item in self.__koleksi
            if not item.is_dipinjam
        ]

        if not item_tersedia:
            print("Tidak ada item yang tersedia.")
            return

        for item in item_tersedia:
            print(item.get_detail())

    def cari_item(self, kata_kunci):
        """Mencari item berdasarkan ID atau judul."""
        hasil = []

        for item in self.__koleksi:
            if (
                str(item._id).lower() == str(kata_kunci).lower()
                or kata_kunci.lower() in item.judul.lower()
            ):
                hasil.append(item)

        if hasil:
            print("\n=== HASIL PENCARIAN ===")
            for item in hasil:
                print(item.get_detail())
        else:
            print("\nItem tidak ditemukan.")

        return hasil
