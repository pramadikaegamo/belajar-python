# belajar tipe data dictionary

customer = {"Name": "Eko", "Age": 30, "Address": "Subang"}

name = customer["Name"]
age = customer["Age"]
address = customer["Address"]

customer["Company"] = "x"
customer["Name"] = "Eko Kurniawan"

del customer["Address"]

for key, value in customer.items():
    print(f"{key}:{value}")
