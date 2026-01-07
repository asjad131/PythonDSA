def serve_chai():
    chai_type = "masala"
    print(f"Inside function type : {chai_type}")

chai_type = "lemon"
serve_chai()
print(f"Outside function type : {chai_type}")

#enclosing scope
def chai_counter():
    chai_order = "lemon"

    def print_order():
        chai_order = "Ginger"
        print(f"Inner: {chai_order}")
    print_order()    
    print(f"Outer : {chai_order}")

chai_order = "tulsi"    
chai_counter()
print(f"Global : {chai_order}")