options = {"a":"Add item", "l":"List items", "q":"Log out"}

def view(description, strings):
    print(description)
    for x in strings:
        print(f"{x})  {strings[x]}")

            
            

view("Select an action", options)

while True:
    action = input("Option: ")
    if action in options:
        print()
        print(f"You selected option {action}) " + options[action])
        print()