values = ["85", "abc", "92", "7x", "40", ""]

# Har value ke liye:

# 1. isdigit() se check kar ki ye number hai ya nahi
# 2. Agar number hai, to int() mein badal ke 80 se compare kar
#    80 se zyada ho to "ALERT", warna "OK" print kar
# 3. Agar number nahi hai, to "Invalid value: <value>" print kar
for value in values:
    if value.isdigit():
        if int(value) > 80:
            print("ALERT")
        else:
            print("OK")
    else:
        print(f"Invalid value: {value}")