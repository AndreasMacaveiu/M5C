users = {"nisse":"apa", "bosse":"ko", "stina":"t-rex"}
data = {"nisse":["vill hem","vill sova"], "bosse":["vill plugga"], "stina":["vill festa"]}
def view(description, strings):
    print(description)
    print()
    for name in strings:
        print(f"   {name}) {strings[name]}")

def view2(description, strings):
    for name in strings:
        return(f"  {description} {strings}")



print()
print("Användare:")
print("         ")
for x in users:
    print(f"    {x}")
print()
print()
view("Användare och Lösenord", users)
print()
print()
view("Användare deras data", data)
print()

while True:
    name = input("Slå upp användare: ")    
    if name in users:
        print(view2((f"Data lagrat för {name}:"), data[name]))
    else:
        print(f"Användaren {name} finns inte")

