import json
import pandas as pd

with open("order.json", "r") as file:
    orders = json.load(file)
    
print("Antal orders:", len(orders))
print("Exempel på en order:")
print(orders[0])

for order in orders:
    print(f"Order ID: {order['order_id']} - Customer: {order['customer']}")
    total_price = 0
    
    for product in order['products']:
        name = product['name']
        price = product['price']
        quantity = product['quantity']
        total_price += price * quantity
        
        print(f"Product: {name:<20} Quantity: {quantity:<5} Price: {price:<10.2f}")
        
    
    print(f"Total price: {total_price:.2f}")
    print("-" * 50)