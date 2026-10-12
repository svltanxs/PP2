with open("sample.txt", "w") as f:
    f.write("Hello\n")
    f.write("This is my first file\n")
    f.write("Python is cool\n")

with open("sample.txt", "a") as f:
    f.write("This line was added later\n")

with open("sample.txt") as f:
    print(f.read())

try:
    with open("new_file.txt", "x") as f:
        f.write("created with x mode\n")
    print("new_file.txt created")
except FileExistsError:
    print("new_file.txt already exists")
