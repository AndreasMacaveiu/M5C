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
    n = 5
    while n > 0:
        name = input(prompt)
        strings.append(name)
        n += -1
    while n == 0:
        view("Du har matat in följande 5 strängar", strings)
        break

add("Lägg till en sträng: ", strings)
