# Write a Python program that calculates movie ticket costs with different pricing.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
quantity = int(input("How many tickets would you like to reserve? "))


if age <= 13:
    ticket_type = "Child"
    ticket_price = 8.00
elif age <= 64:
    ticket_type = "Adult"
    ticket_price = 12.00
else:
    ticket_type = "Senior"
    ticket_price = 9.00


total_cost = ticket_price * quantity


print(f"Customer: {name}")
print(f"Ticket Type: {ticket_type} (${ticket_price:.2f} each)")
print(f"Quantity: {quantity}")
print(f"Total Cost: ${total_cost:.2f}")
print("Thank you for your purchase!")
