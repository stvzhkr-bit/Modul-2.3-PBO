class Mahasiswa:
    def __init__(self, nim, nama, semester, ipk):
        self.nim = nim             # public
        self.nama = nama           # public
        self._semester = semester  # protected
        self.__ipk = ipk           # private

    # Getter semester
    def get_semester(self):
        return self._semester

    # Setter semester
    def set_semester(self, nilai):
        if nilai <= 0:
            raise ValueError("Semester harus lebih dari 0")
        self._semester = nilai

    # Getter IPK
    def get_ipk(self):
        return self.__ipk

    # Setter IPK
    def set_ipk(self, nilai):
        if not (0.0 <= nilai <= 4.0):
            raise ValueError("IPK harus 0.0 - 4.0")
        self.__ipk = round(nilai, 2)


# ====================================
# b. Membuat 2 objek Mahasiswa
# ====================================
m1 = Mahasiswa("23001", "Budi", 2, 3.2)
m2 = Mahasiswa("23002", "Siti", 4, 3.8)

print("=== Data Mahasiswa Awal ===")
print(m1.nim, m1.nama, m1.get_semester(), m1.get_ipk())
print(m2.nim, m2.nama, m2.get_semester(), m2.get_ipk())

# ====================================
# c. Mengganti semester dan IPK
# ====================================
m1.set_semester(3)
m1.set_ipk(3.75)

m2.set_semester(5)
m2.set_ipk(3.90)

print("\n=== Data Mahasiswa Setelah Diubah ===")
print(m1.nim, m1.nama, m1.get_semester(), m1.get_ipk())
print(m2.nim, m2.nama, m2.get_semester(), m2.get_ipk())