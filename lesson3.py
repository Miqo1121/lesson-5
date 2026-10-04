# price = float(input("ყიდვის თანხა (ლარი): "))
# promo = input("პრომო-კოდი (თუ არ გაქვთ — Enter): ")

# if price >= 200:
#     discount = 20

# elif price >= 100:
#     discount = 10

# elif price >= 50:
#     discount = 5

# else:
#     discount = 0

# disocunted = price * (100 - discount) /100

# if promo == "vip":
#     disocunted -= 5
#     print("🎖 VIP კოდი: დამატებით -5 ლარი: ")

# print("ფასდაკლება: ", discount, "%")
# print("გადასახდელი: ", round(disocunted, 2), "ლარი")


print("=== შეფასების სისტემა ===")
try:
    name = input("სტუდენტის სახელი: ") . strip()
    score = float(input("მიღებული ქულა: "))
    most_score = float(input("მაქსიმალური ქულა: "))

    if name == "":
        raise ValueError("სახელი ცარიელია")
    if most_score <= 0:
        raise ValueError("მაქსიმალური ქულა 0 ან ნაკლები უნდა არ იყოს")
    if score <0 or score > most_score:
        raise ValueError("ქულა არასწორ დიაპაზონშია")

except ValueError as e:
    print("❌", e)


else:
    percent = score / most_score * 100

    if percent >= 91:
        grade = "A"
    elif percent >= 81:
        grade = "B"
    elif percent >= 71:
        grade = "C"
    elif percent >= 61:
        grade = "D"
    elif percent >= 51:
        grade = "E"
    elif percent >= 41:
        grade = "FX"

    else:
        grade = "F"

    print(f" {name} — {percent:.1f}% — შეფასება: {grade}")

finally:
    print("შეფასების სისტემა დასრულდა")
