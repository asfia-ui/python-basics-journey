# lists_basics.py

sales = [1500, 2300, 1800, 4200, 3100]

print("First sale:", sales[0])
print("Last sale:", sales[-1])
print("Middle sales:", sales[1:3])

print("Total entries:", len(sales))
print("Total sales:", sum(sales))
print("Highest sale:", max(sales))
print("Lowest sale:", min(sales))