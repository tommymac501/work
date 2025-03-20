
import json

# Open and read the JSON file
with open("https://github.com/tommymac501/work/sales.json", "r") as file:
    sales_data = json.load(file)

# Now sales_data is a list of dictionaries, ready for analysis
print("Data loaded successfully!")
print(sales_data)