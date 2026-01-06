names =["Asjad", "Nikunj", "Surajit", "Mahesh"]
bills = [100, 200,250, 150]

for name, amount in zip(names,bills):
    print(f" {name} paid {amount} rupees.")