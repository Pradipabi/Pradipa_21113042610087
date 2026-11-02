guests = ["Dipa", "Abi", "Citra"]

print(f"{guests[1]} tidak bisa menghadiri makan malam.")

guests[1] = "Dimas"

print("\nUndangan baru:")

for guest in guests:
    print(f"Halo {guest}, saya mengundangmu untuk makan malam.")