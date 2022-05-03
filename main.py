def add():
    b = input("Vase jmeno: ")
    c = input("Vase heslo: ")
    d = f"{b} {c}"
    with open('readme.txt', 'a') as f:
        f.write('\n'.join(d))


def view():
    pass


a = input("add/view/q: ").lower()
if a == "add":
    add()
if a == "view":
    pass
if a == "q":
    quit()