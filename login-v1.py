users = {"nisse":"apa", "bosse":"ko", "stina":"t-rex"}

while True:
    user = input("User: ")
    guess = input("Password: ")
    if users[user] == guess:
            print(f"Welcome {user}")
    else:
         print("YOU FRAUD")
