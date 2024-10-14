def login(users):
    while True:
        user = input("User: ")
        guess = input("Password: ")
        if user in users:
            if users[user] == guess:
                return user
            else:("YOU FRAUD")
        else:
             print("You are not real")

users1 = {"nisse":"apa", "bosse":"ko", "stina":"t-rex"}
user1 = login(users1)
print(f"Welcome {user1}")

users2 = {"foo":"123", "bar":"hello", "foobar":"hello123"}
user2 = login(users2)
print(f"Welcome {user2}")