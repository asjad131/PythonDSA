value = 13
#reminder = value % 5

#if reminder:
    #print(f"1.Not divisible. Reminder is {reminder}")

if (reminder := value % 5):
    print(f"Not divisible. Reminder is {reminder}")

#example
available_sizes = ["small", "medium", "large"]
if (requested_size := input(f"Enter your cup size: ")) in available_sizes:
    print(f"serving requested Size :{requested_size}")
else:
    print(f"Unavailable Size: {requested_size}") 


#example3
flavors = ["ginger", "masala", "lemon", "mint"]
print(f"Available tea falvors: {flavors}")   

while ( flavor := input("Choose your flavor: ")) not in flavors:
    print(f"Sorry, {flavor} flavor is npot available.")

print(f"You chose {flavor} flavor.")
print(f"serving {requested_size} {flavor} chai.")       