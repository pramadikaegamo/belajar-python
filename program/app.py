# program management kontak

import function

# list of dictionary
daftar_kontak = []
daftar_kontak.append(
    {
        "nama": "Pramadika Egamo",
        "email": "dikaegamo1@gmail.com",
        "telepon": "082216322222",
    }
)

# menu program
while True:
    print("\n<<<<<<<< MENU >>>>>>>>>")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Hapus Kontak")
    print("4. Cari Kontak")
    print("0. Keluar Program")
    print("<<<<<<<< MENU >>>>>>>>>")

    menu = int(input("Pilih menu : "))

    if menu == 0:
        break
    elif menu == 1:
        function.display_kontak(daftar_kontak)
    elif menu == 2:
        kontak = function.new_kontak()
        daftar_kontak.append(kontak)
    elif menu == 3:
        function.hapus_kontak(daftar_kontak)
    elif menu == 4:
        function.cari_kontak(daftar_kontak)
    else:
        print("Menu tidak tersedia")


print("Program selesai, sampai jumpa")
