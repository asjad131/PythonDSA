chai_type = "ginger"
print(f"Initial Value = {chai_type}")
def front_desk():
    def kitchen():
        global chai_type
        chai_type = "Irani"

    kitchen()
front_desk()
print(f"Final Value: {chai_type}")        