# belajar module


def say_hello(nama):
    return f"Hello {nama}"


def total(*list_angka):
    hasil = 0
    for i in list_angka:
        hasil += i
    return hasil
