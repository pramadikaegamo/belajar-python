# belajr set

# list => []
# tuple => ()
# set => {} cocok untuk menyimpan data yang unik dan tidak bisa pengambilan data menggunakan index

nama = {"eko", "joko", "eko", "joko", "andi"}

nama.add("kurniawan")
nama.add("kurniawan")
nama.add("kurniawan")

for i in nama:
    print(i)

nama.remove("eko")
nama.remove("andi")
print(nama)
