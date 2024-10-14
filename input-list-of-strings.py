empty = []

n = 5

def add(prompt, strings):
    name = input(prompt)
    strings.append(name)
    return strings

def view(description, strings):
    print(description)
    n = 1
    for x in strings:
        print(f"{n})  {x}")
        n +=1

print(f"Du har matat in földjande {n} sträng(ar)")
add("Lägg till en sträng", empty)
