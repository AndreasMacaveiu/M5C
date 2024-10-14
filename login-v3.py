options1 = {"a":"Add item", "l":"List items", "q":"Log out"}
options2 = {"r":"Try again", "q":"Quit"}
users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}

def view(description, strings):
    print(description)
    for x in strings:
        print(f"{x})  {strings[x]}")

def menu(title, prompt, options):
    view(title, options)
    action = input(prompt)
    if action in options:
       return action

def login(users):
    while True:
        user = input("User: ")
        guess = input("Password: ")
        if user in users:
            if users[user] == guess:
                return user
            else:
                action = menu("Invalid username or password", "Option: ", options2)
                if action == "q":
                    user = None
                    break
        else:
             action = menu("Invalid username or password", "Option: ", options2)
             if action == "q":
                user = None
                break




