import os

path = input("Path: ")

print("Directories:")
for name in os.listdir(path):
    if os.path.isdir(os.path.join(path, name)):
        print(name)

print("Files:")
for name in os.listdir(path):
    if os.path.isfile(os.path.join(path, name)):
        print(name)

print("All:")
for name in os.listdir(path):
    print(name)
