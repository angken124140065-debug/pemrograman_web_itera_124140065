
from abc import ABC, abstractmethod


class LibraryItem(ABC):
    """Abstract class sebagai dasar item perpustakaan."""

    def __init__(self, id_item, judul):
        self._id = id_item
        self._judul = judul
        self.__dipinjam = False

    @property
    def judul(self):
        """Mengambil judul item."""
        return self._judul

    @property
    def is_dipinjam(self):
        """Menampilkan status peminjaman item."""
        return self.__dipinjam

    def pinjam(self):
        """Mengubah status item menjadi dipinjam."""
        if not self.__dipinjam:
            self.__dipinjam = True
            return True
        return False

    def kembalikan(self):
        """Mengubah status item menjadi tersedia."""
        if self.__dipinjam:
            self.__dipinjam = False
            return True
        return False

    @abstractmethod
    def get_detail(self):
        """Menampilkan informasi detail item."""
        pass

    @abstractmethod
    def hitung_denda(self, hari):
        """Menghitung denda keterlambatan."""
        pass


class Book(LibraryItem):
    """Class untuk menyimpan data buku."""

    def __init__(self, id_item, judul, penulis):
        super().__init__(id_item, judul)
        self._penulis = penulis

    def get_detail(self):
        """Menampilkan detail buku."""
        status = "Dipinjam" if self.is_dipinjam else "Tersedia"
        return (
            f"[Buku] ID: {self._id} | Judul: {self._judul} | "
            f"Penulis: {self._penulis} | Status: {status}"
        )

    def hitung_denda(self, hari):
        """Menghitung denda buku sebesar Rp1.000 per hari."""
        return max(0, hari) * 1000


class Magazine(LibraryItem):
    """Class untuk menyimpan data majalah."""

    def __init__(self, id_item, judul, edisi):
        super().__init__(id_item, judul)
        self._edisi = edisi

    def get_detail(self):
        """Menampilkan detail majalah."""
        status = "Dipinjam" if self.is_dipinjam else "Tersedia"
        return (
            f"[Majalah] ID: {self._id} | Judul: {self._judul} | "
            f"Edisi: {self._edisi} | Status: {status}"
        )

    def hitung_denda(self, hari):
        """Menghitung denda majalah sebesar Rp500 per hari."""
        return max(0, hari) * 500
