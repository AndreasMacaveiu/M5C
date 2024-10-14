options = {"a":"Add item", "l":"List items", "q":"Log out"}

def view(description, strings):
    print(description)
    for x in strings:
        print(f"{n})  {x}")
        
def menu():
    view("Select an action", {options})
        