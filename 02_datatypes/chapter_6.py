chai_type = 'Ginger Chai'
customer_name = "Asjad"

print(f"Order for {customer_name} : {chai_type} please!")

chai_desc = "Aromatic and Bold"
print(f"First Word: {chai_desc[:8]}")
print(f"Last Word: {chai_desc[12:]}")
print(f"Reverse Word: {chai_desc[::-1]}")
print(f"Step Word: {chai_desc[:8:2]}")

label_text = "Chai Spécial"
encoded_label = label_text.encode("utf-8")
print(f"Non-encode label : {label_text}")
print(f"encoded label : {encoded_label}")
decoded_label = encoded_label.decode("utf-8")
print(f"decoded label : {decoded_label}")