guests = ["Dipa", "Dimas", "Citra"]

print("Saya menemukan meja makan yang lebih besar!")

guests.insert(0, "Eka")

middle_index = len(guests) // 2
guests.insert(middle_index, "Fajar")

guests.append("Gilang")

print("\nDaftar undangan baru:")

for guest in guests:
    print(f"Halo {guest}, kamu diundang makan malam.")