# belajar method return value


def jumlahkan(*list_angka):
    total = 0
    for i in list_angka:
        total += i
    return (list_angka, total)


list_angka, total = jumlahkan(10, 10, 10, 10)

# mengambil data total?
print(f"total {list_angka} = {total}")
