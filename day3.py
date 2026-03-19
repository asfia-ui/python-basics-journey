# A dictionary = labeled data
#example1
customer = {
    "name": "Priya",
    "age": 25,
    "city": "Hyderabad",
    "purchases": 8
}

print(customer["name"])      # Priya
print(customer["purchases"]) # 8

# Add a new field
customer["vip"] = True
print(customer)

# Loop through a dictionary
for key, value in customer.items():
    print(f"{key}: {value}")

#example2
# # Creating a dictionary
product = {
    "name": "Laptop",
    "price": 50000,
    "category": "Electronics",
    "stock": True
}

# Looping through dictionary and printing key-value pairs
for key, value in product.items():
    print(key, ":", value)    