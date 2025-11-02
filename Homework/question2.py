# Create a program that takes a restaurant order and calculates the bill based on menu choices.

print("=== RESTAURANT MENU ===")
print("1. Pizza - $15.99")
print("2. Burger - $12.50")
print("3. Salad - $9.99")
print("4. Pasta - $13.75")

food_option = int(input("Enter your choice (1-4): "))

if food_option == 1:
    food = "Pizza"
    price = 15.99
elif food_option == 2:
    food = "Burger"
    price = 12.50
elif food_option == 3:
    food = "Salad"
    price = 9.99
else:
    food_option == 4
    food = "Pasta"
    price = 13.75

drink = input("Would you like to add a drink for 2.50? yes/no: ")

if drink == "yes":
    drink_price = 2.50
    display_drink = "Yes"
else:
    drink_price = 0.00
    display_drink = "No"

subtotal = price + drink_price
tax = subtotal * 0.08
total = subtotal + tax


print("=== YOUR ORDER ===")
print(f"Food: {food} - ${price}")
print(f"Drink: {display_drink} - ${drink_price:.2f}")
print(f"Subtotal: {subtotal}")
print(f"Tax (8%): {tax}")
print(f"Total: {total}")