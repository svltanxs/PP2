name = input("File name: ")

count = 0
with open(name) as f:
    for line in f:
        count += 1

print("Lines:", count)
