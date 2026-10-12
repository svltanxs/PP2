with open("source.txt", "w") as f:
    f.write("line 1\nline 2\nline 3\n")

with open("source.txt") as src:
    text = src.read()

with open("copy.txt", "w") as dst:
    dst.write(text)

with open("copy.txt") as f:
    print(f.read())
