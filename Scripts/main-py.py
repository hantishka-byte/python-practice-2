name = input("Enter customer name: ")

total = 0
count = 0

while True:
    item = input("Enter item name (or 'done' to finish): ")
    if item == "done":
        break
    price = float(input("Enter price: "))
    total = total + price
    count = count + 1

print("Customer :", name.upper())
print("Items :", count)
print("Subtotal :", total, "KZT")

hour = int(input("Enter current hour (0-23): "))


if 6 <= hour < 12:
    discount_name = "Morning discount"
    discount = total * 0.10
elif 12 <= hour < 17:
    discount_name = "No discount"
    discount = 0
elif 17 <= hour < 22:
    discount_name = "Evening discount"
    discount = total * 0.05
else:
    print("Closed")
    print("Name uppercase :", name.upper())
    print("Name lowercase :", name.lower())
    print("Name length :", len(name))
    if name[0].upper() == "A" or name[0].upper() == "S":
        print("VIP customer")
    else:
        print("Regular customer")
    exit()

new_total = total - discount
tip = new_total * 0.10
final_total = new_total + tip

print("Time period :", discount_name)
print("Discount :", discount, "KZT")
print("Tip (10%) :", tip, "KZT")
print("Total :", final_total, "KZT")


