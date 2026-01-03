chai_order = dict(type="Masala Chai", size="large", sugar=2)
print(f"chai order : {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"
print(f"Recpie base : {chai_recipe['base']}")

print(f"Chai Recipe: {chai_recipe}")
del chai_recipe["liquid"]
print(f"Chai Recipe: {chai_recipe}")

print(f" Is Sugar in chai order? : {'sugar' in chai_order}")

print(f"Order Details (keys) : {chai_order.keys()}")
print(f"Order Details (values) : {chai_order.values()}")
print(f"Order Details (items) : {chai_order.items()}")

last_item = chai_order.popitem()
print(f"Last Item: {last_item}")

#print(f" Sugar in the order: {chai_order['sugar']}")
order_sugar = chai_order.get("sugar", "No Sugar")
print(f" Sugar in the order: {order_sugar}")
