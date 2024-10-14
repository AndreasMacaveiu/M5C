names = ["nisse", "stina", "bosse", "mimmi"]

animals = ["Giraff", "Myrslok", "Tapir"]


def view(description, strings):
    print(description)
    n = 1
    for x in strings:
        print(f"{n})  {x}")
        n +=1

view("lista med namn", names)
view("lista med djur", animals)



