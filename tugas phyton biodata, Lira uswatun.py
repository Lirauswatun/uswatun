# Membuat kamus berisi biodata mahasiswa dan nilai matakuliah
mahasiswa = {
    "Lira uswatun hasanah": {
        "nim": "SI19220006",
        "alamat": "Walun",
        "prodi": "SISTEM INFORMASI",
        "semester": 2,
        "ipk": 3.7,
        "nilai_matakuliah": {
            "Aljabar linier":85,
            "Kalkulus": 80,
            "Bahasa_indonesia": 90,
        }
    },
    "Nursahira": {
        "nim": "SI19220021",
        "alamat": "lingkok bunut",
        "prodi": "Sistem Informasi",
        "semester": 2,
        "ipk": 3.8,
        "nilai_matakuliah": {
            "Pemrograman Lanjut": 9.0,
            "Pendidikan anti korupsi": 85 ,
            "Jaringan komputer":90
        }
    },
    "ikhlas nurul islam": {
        "nim": "SI19220005",
        "alamat": "Batu lawang",
        "prodi": "Sistem Informasi",
        "semester": 2,
        "ipk": 3.8,
        "nilai_matakuliah": {
            "algoritma": 70,
            "Multimedia": 85,
            "bahasa inggris": 80
        }
    },
    "sriwahyuni": {
        "nim": "SI19220026",
        "alamat": "lingkok bunut",
        "prodi": "Sistem informasi",
        "semester": 2,
        "ipk": 3.8,
        "nilai_matakuliah": {
            "kalkulus": 90,
            "pkn": 85,
            "struktur data dan algoritma": 95
        }
    },
    "bunga tribuana": {
        "nim": "Si19220030",
        "alamat": "lingkok bunut",
        "prodi": "sistem informasi",
        "semester": 2,
        "ipk": 4.0,
        "nilai_matakuliah": {
            "bahasa indonesia": 90,
            "pemrograman web": 85,
            "integrasi sistem": 95
        }
    }
}

# Menampilkan biodata mahasiswa dan nilai akumulasi tiga matakuliah
for nama, data in mahasiswa.items():
    print("Biodata Mahasiswa")
    print("Nama          :", nama)
    print("NIM           :", data["nim"])
    print("Alamat        :", data["alamat"])
    print("Program Studi :", data["prodi"])
    print("Semester      :", data["semester"])
    print("IPK           :", data["ipk"])
    print("Nilai Akumulasi Matakuliah:")
    total_nilai = 0
    for matakuliah, nilai in data["nilai_matakuliah"].items():
        print("-", matakuliah, ":", nilai)
        total_nilai += nilai
    print("Total Nilai:", total_nilai)
    print("")
