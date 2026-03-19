# For loop — go through every item
sales = [1500, 2300, 1800, 4200, 3100]

for sale in sales:
    print(sale)

# Loop with condition
for sale in sales:
    if sale > 2000:
        print(f"High sale: {sale}")

# Range loop
for i in range(5):
    print(f"Day {i+1}")