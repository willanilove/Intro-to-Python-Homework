# Create a program that converts human years to pet years for different animals.

pet_type = input("Enter pet type (dog/cat/bird/hamster): ")
human_age = int(input("Enter your pet's age in human years: "))

if pet_type in ["dog", "cat"]:
    if human_age <= 2:
        pet_age = human_age * 12
    else:
        pet_age = 24 + (human_age - 2) * 4
elif pet_type == "Bird":
    pet_age = human_age * 9
elif pet_type == "Hamster":
    pet_age = human_age * 25
else:
    pet_age = None

print("\n=== PET AGE CONVERSION ===")
if pet_age is not None:
    print(f"Pet Type: {pet_type}")
    print(f"Human Age: {human_age} years")
    print(f"Pet Age: {pet_age} pet years")
    print(f"\nFun Fact: Your {pet_type} is like a {pet_age}-year-old human!")
