import csv

ahh_data = {
    "jakarta": 85,
    "jawa barat": 80,
    "jawa timur": 78,
    "bali": 82,
    "yogyakarta": 88,
    "sumatera utara": 75
}

def tampilkan_menu():
    print("\n=== MENU ===")
    print("1. Cek AHH Provinsi")
    print("2. Input & Lihat Hobi")
    print("3. Keluar")
    print("4. Tambah AHH Provinsi Baru")
    print("5. Lihat Daftar AHH Provinsi")
    print("6. Simpan AHH ke File CSV")

def cek_ahh_provinsi():
    print("\n=== Cek AHH Provinsi ===")
    provinsi = input("Masukkan nama provinsi: ").lower()
    if provinsi in ahh_data:
        print(f"AHH Provinsi {provinsi.title()}: {ahh_data[provinsi]}")
    else:
        print(f"Maaf, data AHH untuk provinsi {provinsi.title()} tidak tersedia.")

def input_dan_lihat_hobi():
    print("\n=== Input & Lihat Hobi ===")
    hobby_input = input("Masukkan hobi Anda (pisahkan dengan koma): ")
    hobby_list = hobby_input.split(", ")

    print("\n=== Daftar Hobi Kamu ===")
    for i, hobi in enumerate(hobby_list, start=1):
        print(f"{i}. Hobi saya adalah {hobi}.")

    with open("hobi.txt", "w") as file:
        for hobi in hobby_list:
            file.write(f"{hobi}\n")

    try:
        with open("hobi.txt", "r") as file:
            print("\n=== Hobi Anda ===")
            for line in file:
                print(f"- {line.strip()}")
    except FileNotFoundError:
        print("File 'hobi.txt' tidak ditemukan. Membuat file baru...")

    print("\nHobi Anda telah disimpan ke dalam file 'hobi.txt'.")

def tambah_ahh_provinsi():
    print("\n=== Tambah AHH Provinsi Baru ===")
    prov = input("Masukkan nama provinsi baru: ").lower()
    angka = float(input("Masukkan AHH-nya: "))
    ahh_data[prov] = angka
    print(f"✅ Data AHH untuk {prov.title()} disimpan!")

def lihat_semua_ahh():
    print("\n=== Daftar AHH Provinsi ===")
    for nama, nilai in ahh_data.items():
        print(f"- {nama.title()}: {nilai}")

def simpan_ahh_ke_csv():
    print("\n=== Simpan AHH ke File CSV ===")
    with open("ahh_data.csv", "w", newline='') as csvfile:
        fieldnames = ['Provinsi', 'AHH']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for provinsi, ahh in ahh_data.items():
            writer.writerow({'Provinsi': provinsi.title(), 'AHH': ahh})
    print("✅ Data AHH telah disimpan ke dalam file 'ahh_data.csv'.")

print("=== Selamat Datang di Program Adit Assistant v3.0 ===")

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        cek_ahh_provinsi()
    elif pilihan == "2":
        input_dan_lihat_hobi()
    elif pilihan == "3":
        print("Terima kasih telah menggunakan program ini! 👋")
        break
    elif pilihan == "4":
        tambah_ahh_provinsi()
    elif pilihan == "5":
        lihat_semua_ahh()
    elif pilihan == "6":
        simpan_ahh_ke_csv()
    else:
        print("Pilihan tidak valid, coba lagi ya!")
