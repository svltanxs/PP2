with open("sample.txt", "w") as f:
    f.write("first line\nsecond line\nthird line\n")

with open("sample.txt") as f:
    print(f.read())

with open("sample.txt") as f:
    print(f.readline())
    print(f.readline())

with open("sample.txt") as f:
    lines = f.readlines()
print(lines)

with open("sample.txt") as f:
    for line in f:
        print(line.strip())
