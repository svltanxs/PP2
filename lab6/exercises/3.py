import os

path = input("Path: ")

if os.path.exists(path):
    print("Path exists")
    print("File name:", os.path.basename(path))
    print("Directory:", os.path.dirname(path))
else:
    print("Path does not exist")
