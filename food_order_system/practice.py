print("Welcome to my restaurent, Here's the menu: ")
Pizza = 40
print('Pizza: ', Pizza)
Pasta = 80
print("Pasta: ", Pasta)
Burger = 60
print("Burger: ", Burger)


a = input("Enter Item you want to order = ")
if(a == 'Pizza'):
    print(f"Order of {a} has been added")
elif(a == 'Pasta'):
    print(f"Order of {a} has been added")
elif(a == 'Burger'):
    print(f"Order of {a} has been added")
else:
    print("Please order something from the menu")
response = input('Do you want to order anything else? (yes/no) = ')


if response.lower() == 'yes':
    b = input("Enter second Item you want to order = ")
    if(b == 'Pizza'):
        print(f"Order of {b} has been added")
    elif(b == 'Pasta'):
        print(f"Order of {b} has been added")
    elif(b == 'Burger'):
        print(f"Order of {b} has been added")
    else:
        print("Please order something from the menu")
else:
    b = None


total = 0
if a == 'Pizza':
    total += Pizza
elif a == 'Pasta':
    total += Pasta
elif a == 'Burger':
    total += Burger

if b == 'Pizza':
    total += Pizza
elif b == 'Pasta':
    total += Pasta
elif b == 'Burger':
    total += Burger

print(f'The total price of your order is {total} ruppes')