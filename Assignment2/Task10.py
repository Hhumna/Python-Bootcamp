size = int(input(
    "Select Pizza Size:\n"
    "1. Small Pizza: $15\n"
    "2. Medium Pizza: $20\n"
    "3. Large Pizza: $25\n"
))


if (size == 1):
    sum = 15
    add_pepperoni = input("\nAdd Pepperoni for Small Pizza: +$2 (Y/N)? ")
    if (add_pepperoni == "Y" or add_pepperoni == "y"):
        sum += 2
    add_extra_cheese = input("\nAdd Extra Cheese: +$1 (Y/N)? ")
    if (add_extra_cheese == "Y" or add_extra_cheese == "y"):
        sum += 1
    print("Your final bill is: $" + str(sum))


elif (size == 2):
    sum = 20
    add_pepperoni = input("\nAdd Pepperoni for Medium Pizza: +$3 (Y/N)? ")
    if (add_pepperoni == "Y" or add_pepperoni == "y"):
        sum += 3
    add_extra_cheese = input("\nAdd Extra Cheese: +$1 (Y/N)? ")
    if (add_extra_cheese == "Y" or add_extra_cheese == "y"):
        sum += 1
    print("Your final bill is: $" + str(sum))
elif (size == 3):
    sum = 25
    add_pepperoni = input("\nAdd Pepperoni for Large Pizza: +$3 (Y/N)? ")
    if (add_pepperoni == "Y" or add_pepperoni == "y"):
        sum += 3
    add_extra_cheese = input("\nAdd Extra Cheese: +$1 (Y/N)? ")
    if (add_extra_cheese == "Y" or add_extra_cheese == "y"):
        sum += 1
    print("Your final bill is: $" + str(sum))
else:
    print("Invalid choice.")