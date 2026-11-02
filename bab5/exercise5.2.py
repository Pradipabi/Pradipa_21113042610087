car = "Toyota"
age = 20
numbers = [1, 2, 3, 4, 5]

# Kesamaan string
print(car == "Toyota")

# Ketidaksamaan string
print(car != "Honda")

# Perbandingan tanpa membedakan huruf besar-kecil
print(car.lower() == "toyota")

# Perbandingan angka
print(age > 18)
print(age < 25)
print(age >= 20)
print(age <= 20)

# Menggunakan and
print(age > 18 and age < 25)

# Menggunakan or
print(age < 18 or age == 20)

# Memeriksa keberadaan angka
print(3 in numbers)

# Memeriksa angka yang tidak tersedia
print(10 not in numbers)