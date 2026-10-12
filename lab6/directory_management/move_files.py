import os
import shutil
from pathlib import Path

os.makedirs("from_dir", exist_ok=True)
os.makedirs("to_dir", exist_ok=True)

with open("from_dir/file1.txt", "w") as f:
    f.write("file 1")
with open("from_dir/file2.txt", "w") as f:
    f.write("file 2")

shutil.copy("from_dir/file1.txt", "to_dir/file1.txt")
shutil.move("from_dir/file2.txt", "to_dir/file2.txt")

print("from_dir:", os.listdir("from_dir"))
print("to_dir:", os.listdir("to_dir"))

for p in Path("to_dir").glob("*.txt"):
    print(p.name)
