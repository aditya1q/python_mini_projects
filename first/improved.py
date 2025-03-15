def display_menu():
    menu = {
        'Pizza': 40,
        'Pasta': 80,
        'Burger': 60
    }
    print("Welcome to my restaurant, Here's the menu:")
    for item, price in menu.items():
        print(f"{item}: {price}rs")
    return menu

def take_order(menu):
    orders = []
    while True:
        item = input("Enter item you want to order (or 'done' to finish) = ").capitalize()
        if item == 'Done':
            break
        if item in menu:
            print(f"Order of {item} has been added")
            orders.append(item)
        else:
            print("Please order something from the menu")
    
    total = sum(menu[item] for item in orders)
    return orders, total

def main():
    menu = display_menu()
    orders, total = take_order(menu)
    
    if orders:
        print("\nYour order summary:")
        for item in orders:
            print(f"- {item}")
        print(f"Total price: {total}rs")
    else:
        print("No items ordered")

if __name__ == "__main__":
    main()