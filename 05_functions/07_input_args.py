chai = "ginger"

def prepare_chai(order):
    print("Preparing ", order)

prepare_chai(chai)
print(chai)

 #mutable
chai_list = [1,2,3]
print( f"chai list: {chai_list}")   

def prepare_list_chai(order):
    chai_list[1]= 4

prepare_list_chai(chai_list)    
print( f"chai list: {chai_list}")    

def make_chai(tea, milk, sugar):
    print(tea, milk,sugar)

make_chai("Darjeelimg", "Yes", "Low") #positional
make_chai(tea = "Green", sugar="Medium", milk="Low") #keywords

def special_chai(*ingredients, **extras):
    print(f"Ingredients : ", ingredients)
    print(f"EXtras : ", extras)

special_chai("cinnamon", "cardamom", sweetener = "honey", foam="yes")

def chai_order(order = None):
    if order is None:
        order = []
    print(order)

chai_order()
chai_order()    