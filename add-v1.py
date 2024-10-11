ducks = ["Huey", "Dewey", "Louie"]
composers = ["Mozart", "Bach", "Liszt"]

def add(prompt, strings):
    name = input(prompt)
    strings.append(name)
    return strings

print(f"  : {ducks}")


print("List of ducks: ", ducks)

print("             ")

add(" add a duck: ", ducks)

print("			")
print(f"  Ducks: {ducks}")
print("			")

print("Composers :", composers)

print("			")

add("WHO WROTE THE 9TH SYMPHONY: ", composers,)

print(f"Composers : {composers}")