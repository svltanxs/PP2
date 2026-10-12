import os

path = input("Path: ")

if os.path.exists(path):
    if os.access(path, os.W_OK):
        os.remove(path)
        print("Deleted")
    else:
        print("No access")
else:
    print("File not found")
