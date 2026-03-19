# Define a function
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# Call it
marks = [72, 85, 90, 61, 78]
avg = calculate_average(marks)
print(f"Average marks: {avg}")

# A more data-focused function
def sales_summary(sales):
    print(f"Total sales:   {sum(sales)}")
    print(f"Average sale:  {sum(sales)/len(sales):.2f}")
    print(f"Best day:      {max(sales)}")
    print(f"Worst day:     {min(sales)}")

monthly_sales = [1500, 2300, 1800, 4200, 3100, 2750]
sales_summary(monthly_sales)