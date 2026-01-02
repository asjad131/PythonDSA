ingredients = ["water", "tea", "milk"]
ingredients.append("sugar")
print(f"ingredients are : {ingredients}")
ingredients.remove("water")
print(f"ingredients are : {ingredients}")

chai_ingredients = ["water", "milk", "tea"]
spice_options = ["ginger","cardamom"]
chai_ingredients.extend(spice_options)
print(f"Chai Ingredients are: {chai_ingredients}")

chai_ingredients.insert(2, "sugar")
print(f"Chai Ingredients are: {chai_ingredients}")

last_added = chai_ingredients.pop()
print(f"popped : {last_added}")
print(f"Chai Ingredients are: {chai_ingredients}")

chai_ingredients.reverse()
print(f"Chai Ingredients are: {chai_ingredients}")

chai_ingredients.sort()
print(f"Chai Ingredients are: {chai_ingredients}")

sugar_levels = [1,2,3,4,5]
print(f"Maximum Sugar Level : {max(sugar_levels)}")
print(f"Minimum Sugar Level : {min(sugar_levels)}")

base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]
full_liquid_mix = base_liquid + extra_flavor
print(f"Liquid Mix : {full_liquid_mix}")

strong_brew = ["black tea", "water"] * 3
print(f"Strong Brew: {strong_brew}")
