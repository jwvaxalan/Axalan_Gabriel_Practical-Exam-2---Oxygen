def generate_receipt(ordered_items):
    #  receipt display
    print("\n" + "=" * 40)
    print("             OFFICIAL RECEIPT")
    print("=" * 40)
    print(f"{'Item':<16} {'Qty':<5} {'Price':<8} {'Subtotal':<8}")
    print("-" * 40)
    
    total_amount = 0.0
    
    
    if not ordered_items:
        print("No items ordered.")
    else:
        for item in ordered_items:
            name = item["name"]
            qty = item["quantity"]
            price = item["price"]
            subtotal = item["subtotal"]
            
            total_amount += subtotal
            print(f"{name:<16} {qty:<5} {price:<8.2f} {subtotal:<8.2f}")
            
    print("-" * 40)
    print(f"{'TOTAL AMOUNT:':<30} PHP {total_amount:.2f}")
    print("=" * 40)
    print("       Thank you for your purchase!\n")
    
    return total_amount

# example ko 
if __name__ == "_main_":
    sample_orders = [
        {"name": "Burger", "price": 85.00, "quantity": 2, "subtotal": 170.00},
        {"name": "Soda", "price": 35.00, "quantity": 1, "subtotal": 35.00}
    ]
    generate_receipt(sample_orders)
