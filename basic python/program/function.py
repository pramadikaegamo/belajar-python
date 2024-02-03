# program management kontak


def display_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print("==================================")
        print(f"nama\t: {kontak['nama']}")
        print(f"Email\t: {kontak['email']}")
        print(f"Telepon\t: {kontak['telepon']}")


def new_kontak():
    nama = input("nama\t: ")
    email = input("email\t: ")
    telepon = input("Telepon\t: ")
    kontak = {"nama": nama, "email": email, "telepon": telepon}
    return kontak


def hapus_kontak(daftar_kontak):
    nama = input("Nama kontak yang akan di hapus : ")
    index = -1
    for i in range(0, len(daftar_kontak)):
        kontak = daftar_kontak[i]
        if nama == kontak["nama"]:
            index = i
            break
    if index == -1:
        print("Data tidak ditemukan")
    else:
        del daftar_kontak[i]
    print("Berhasil menghapus kontak")


def cari_kontak(daftar_kontak):
    nama_yang_dicari = input("Nama kontak yang di cari : ")
    for kontak in daftar_kontak:
        nama = kontak["nama"]
        if nama.lower().find(nama_yang_dicari.lower()) != -1:
            print("==================================")
            print(f"nama\t: {kontak['nama']}")
            print(f"Email\t: {kontak['email']}")
            print(f"Telepon\t: {kontak['telepon']}")
