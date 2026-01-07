def add_vat(price, vat_rate):
    return price * (100 + vat_rate)/100

prices = [150, 250, 500]
for price in prices:
    final_amount = add_vat(price, 10)
    print(f"Original Price: {price} Final Price: {final_amount}")