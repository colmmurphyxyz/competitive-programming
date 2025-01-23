import sys

name: str = sys.stdin.readline().strip()
first_letter: str = name[0].lower()

first: str = "b" + name[1:]
if first_letter == "b":
    first = name[1:]

second: str = "f" + name[1:]
if first_letter == "f":
    second = name[1:]

third: str = "m" + name[1:]
if first_letter == "m":
    third = name[1:]

print(f"{name}, {name}, bo-{first}")
print(f"bo-na-na fanna, fo-{second}")
print(f"fee fi mo-{third}, {name}!")
