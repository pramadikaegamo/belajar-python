# belajr argument list
# cuman bisa satu / disimpan di paramter paling belakang


def jumlahkan(*list_angka):
    total = 0
    for i in list_angka:
        total += i
    print(f"Total {list_angka} = {total}")


jumlahkan(10, 10)
