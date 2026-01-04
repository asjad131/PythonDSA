cup_size = input(f"Please enter your Cup Size (small/Medium/Large):").lower()

if cup_size == "small":
    print(f"Price is Rupess 10.")
elif cup_size == "medium":
    print(f"Price is Rupess 15.")
elif cup_size == "large":
    print(f"Price is Rupees 20.")
else:
    print(f"Unknown cup size!")    