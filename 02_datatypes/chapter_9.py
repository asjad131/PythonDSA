essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "pepper"}

all_spices = essential_spices | optional_spices
print(f"All Spices: {all_spices}")

common_spices = essential_spices & optional_spices
print(f"common Spices: {common_spices}")

only_essential_spices = essential_spices - optional_spices
print(f"common Spices: {only_essential_spices}")

print(f" Is ginger in essential Spices? {'ginger' in essential_spices}")