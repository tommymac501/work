
import json

# The sample sales data
sales_data = [
    {"order_id": "ORD001", "customer": "Alice Smith", "product": "Laptop", "quantity": 1, "price": 999.99, "date": "2025-01-15"},
    {"order_id": "ORD002", "customer": "Bob Johnson", "product": "Mouse", "quantity": 3, "price": 19.99, "date": "2025-02-10"},
    {"order_id": "ORD003", "customer": "Charlie Brown", "product": "Keyboard", "quantity": 2, "price": 49.99, "date": "2025-02-15"},
    {"order_id": "ORD004", "customer": "Alice Smith", "product": "Monitor", "quantity": 1, "price": 149.99, "date": "2025-03-01"},
    {"order_id": "ORD005", "customer": "Dana Lee", "product": "Laptop", "quantity": 2, "price": 999.99, "date": "2025-03-10"}
]

# Write to sales.json
with open("sales.json", "w") as file:
    json.dump(sales_data, file, indent=4)  # indent=4 makes it human-readable

import json

# Open and read the JSON file
with open("sales.json", "r") as file:
    sales_data = json.load(file)

# Now sales_data is a list of dictionaries, ready for analysis
print("Data loaded successfully!")
print(sales_data)

total_revenue = sum(order["quantity"] * order["price"] for order in sales_data)
print(f"Total Revenue: ${total_revenue:.2f}")

alice_orders = [order for order in sales_data if order["customer"] == "Alice Smith"]
print("Alice's Orders:", alice_orders)

# Total Quantity of Laptops Sold
total_laptops = sum(order["quantity"] for order in sales_data if order["product"] == "Laptop")
print("Quatitiy of Laptops Sold:", total_laptops)

