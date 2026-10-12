import os

print(os.getcwd())

os.makedirs("test_dir/a/b", exist_ok=True)

with open("test_dir/one.txt", "w") as f:
    f.write("1")
with open("test_dir/two.py", "w") as f:
    f.write("print(2)")
with open("test_dir/three.txt", "w") as f:
    f.write("3")

print(os.listdir("test_dir"))

for name in os.listdir("test_dir"):
    if name.endswith(".txt"):
        print(name)

if not os.path.exists("empty_dir"):
    os.mkdir("empty_dir")
print(os.path.exists("empty_dir"))
os.rmdir("empty_dir")
print(os.path.exists("empty_dir"))

os.chdir("test_dir")
print(os.getcwd())
os.chdir("..")
print(os.getcwd())
