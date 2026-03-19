#if/else decision making 
#example 1
sales_today = 3200
target = 3000

if sales_today >= target:
    print("Target met!")
elif sales_today >= target * 0.8:
    print("Close — within 80% of target")
else:
    print("Below target")

#example 2
marks = 80

if marks > 75:
    print("Distinction")
elif marks > 40:
    print("Pass")
else:
    print("Fail")    