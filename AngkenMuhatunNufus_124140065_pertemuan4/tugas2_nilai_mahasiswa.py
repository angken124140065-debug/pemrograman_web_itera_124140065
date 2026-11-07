
daftar_mahasiswa = [
    {
        "nama": "Andi",
        "nim": "124140101",
        "nilai_uts": 85,
        "nilai_uas": 90,
        "nilai_tugas": 88
    },
    {
        "nama": "Budi",
        "nim": "124140102",
        "nilai_uts": 75,
        "nilai_uas": 80,
        "nilai_tugas": 78
    },
    {
        "nama": "Citra",
        "nim": "124140103",
        "nilai_uts": 65,
        "nilai_uas": 70,
        "nilai_tugas": 72
    },
    {
        "nama": "Dina",
        "nim": "124140104",
        "nilai_uts": 55,
        "nilai_uas": 60,
        "nilai_tugas": 58
    },
    {
        "nama": "Eko",
        "nim": "124140105",
        "nilai_uts": 40,
        "nilai_uas": 45,
        "nilai_tugas": 48
    }
]

print("=== DATA NILAI MAHASISWA ===")
print(f"{'Nama':<10} {'NIM':<12} {'Akhir':>8} {'Grade':>7}")
print("-" * 42)

for mahasiswa in daftar_mahasiswa:
    nilai_akhir = (
        0.30 * mahasiswa["nilai_uts"]
        + 0.40 * mahasiswa["nilai_uas"]
        + 0.30 * mahasiswa["nilai_tugas"]
    )

    if nilai_akhir >= 80:
        grade = "A"
    elif nilai_akhir >= 70:
        grade = "B"
    elif nilai_akhir >= 60:
        grade = "C"
    elif nilai_akhir >= 50:
        grade = "D"
    else:
        grade = "E"

    mahasiswa["nilai_akhir"] = nilai_akhir
    mahasiswa["grade"] = grade

    print(
        f"{mahasiswa['nama']:<10} "
        f"{mahasiswa['nim']:<12} "
        f"{nilai_akhir:>8.2f} "
        f"{grade:>7}"
    )

nilai_tertinggi = max(
    daftar_mahasiswa,
    key=lambda mahasiswa: mahasiswa["nilai_akhir"]
)

nilai_terendah = min(
    daftar_mahasiswa,
    key=lambda mahasiswa: mahasiswa["nilai_akhir"]
)

print("\n=== HASIL NILAI MAHASISWA ===")
print(
    f"Nilai tertinggi: {nilai_tertinggi['nama']} "
    f"- {nilai_tertinggi['nilai_akhir']:.2f}"
)
print(
    f"Nilai terendah : {nilai_terendah['nama']} "
    f"- {nilai_terendah['nilai_akhir']:.2f}"
)
