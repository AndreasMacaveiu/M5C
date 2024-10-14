strings = []

n = 5
print(f"n = {n}")

def view(description, strings):
    print(description)
    n = 1
    for x in strings:
        print(f"{n})  {x}")
        n +=1



def add(prompt, strings):
    name = input(prompt)
    strings.append(name)
   

while True:
    if n > 0:
        add("Lägg till en sträng: ", strings)
        n += -1
    else:
        view(f"Du har matat in följande {len(strings)} strängar", strings)
        break