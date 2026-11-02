places = [
    "Jepang",
    "Swiss",
    "Prancis",
    "Italia",
    "Korea Selatan"
]

print("Urutan asli:")
print(places)

print("\nUrutan alfabetis:")
print(sorted(places))

print("\nUrutan asli kembali:")
print(places)

print("\nUrutan alfabetis terbalik:")
print(sorted(places, reverse=True))

print("\nUrutan asli kembali:")
print(places)

places.reverse()
print("\nUrutan terbalik permanen:")
print(places)

places.reverse()
print("\nKembali ke urutan asli:")
print(places)

places.sort()
print("\nUrutan alfabetis permanen:")
print(places)

places.sort(reverse=True)
print("\nUrutan alfabetis terbalik permanen:")
print(places)