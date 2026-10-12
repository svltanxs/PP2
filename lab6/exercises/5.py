fruits = ["apple", "banana", "cherry", "orange"]

with open("list.txt", "w") as f:
    for item in fruits:
        f.write(item + "\n")

with open("list.txt") as f:
    print(f.read())
