def calculate_bill(cups , price_per_cup):
    return cups * price_per_cup


my_bill = calculate_bill(3,5.50)
print(f"{my_bill}")

print(f" bill of your order is : " , calculate_bill(5, 25))