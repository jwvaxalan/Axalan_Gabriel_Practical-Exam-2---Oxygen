menu = {
    1: ("Burger", 50.00),
    2: ("Fries", 35.00),
    3: ("Soft Drink", 25.00)
}

def display_menu():
    print("========================================")
    print("       WELCOME TO MINI STORE")
    print("      POS ORDERING SYSTEM")
    print("========================================")
    print("\nPRODUCT MENU")
    print("----------------------------------------")
    for item_id, (name, price) in menu.items():
        print(f"[{item_id}] {name:<12} - PHP {price:.2f}")
    print("----------------------------------------\n")

def take_orders():
    orders = []
    while True:
        try:
            choice = int(input("Enter product number (1-3): "))
            if choice not in menu:
                print("Invalid choice. Please enter 1, 2, or 3.\n")
                continue
            
            qty = int(input("Enter quantity: "))
            if qty <= 0:
                print("Quantity must be at least 1.\n")
                continue

            name, price = menu[choice]
            subtotal = price * qty
            orders.append({
                "name": name,
                "qty": qty,
                "price": price,
                "subtotal": subtotal
            })
            print(f"\nAdded: {name} x {qty}\n")

        except ValueError:
            print("Invalid input. Please enter numbers only.\n")
            continue

        again = input("Order another product? (yes/no): ").strip().lower()
        print()
        if again != "yes":
            break

    return orders

def print_receipt(orders):
    print("========================================")
    print("               RECEIPT")
    print("             MINI STORE")
    print("========================================")
    print(f"{'Product':<12} {'Qty':>4} {'Price':>8} {'Subtotal':>10}")
    print("----------------------------------------")
    
    total_amount = 0.0
    for item in orders:
        print(f"{item['name']:<12} {item['qty']:>4} {item['price']:>8.2f} {item['subtotal']:>10.2f}")
        total_amount += item['subtotal']
        
    print("----------------------------------------")
    print(f"{'TOTAL AMOUNT:':<24} PHP {total_amount:.2f}")
    print("========================================")
    print("      THANK YOU FOR YOUR ORDER!")
    print("========================================")

if __name__ == "_main_":
    display_menu()
    customer_orders = take_orders()
    print_receipt(customer_orders)
