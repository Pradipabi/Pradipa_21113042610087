cars = ["Toyota", "Honda", "BMW", "Suzuki"]

# Menampilkan list
print(cars)

# Mengakses elemen
print(cars[0])

# Mengubah elemen
cars[1] = "Mitsubishi"
print(cars)

# Menambahkan elemen
cars.append("Nissan")
print(cars)

# Menambahkan elemen pada posisi tertentu
cars.insert(1, "Mazda")
print(cars)

# Menghapus elemen
cars.remove("BMW")
print(cars)

# Menghapus elemen berdasarkan index
del cars[0]
print(cars)

# Mengurutkan list
cars.sort()
print(cars)

# Mengurutkan sementara
print(sorted(cars, reverse=True))

# Membalik urutan list
cars.reverse()
print(cars)

print(len(cars))