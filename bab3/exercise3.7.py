guests = [
    "Eka", "Andi", "Fajar",
    "Dimas", "Citra", "Gilang"
]

print("Maaf, saya hanya bisa mengundang dua orang.")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Maaf {removed_guest}, kamu tidak bisa diundang.")

print("\nDua tamu yang tetap diundang:")

for guest in guests:
    print(f"Halo {guest}, kamu tetap diundang.")

del guests[:]

print("\nDaftar tamu setelah dihapus:")
print(guests)