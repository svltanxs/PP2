import os
import shutil

with open("data.txt", "w") as f:
    f.write("some important data\n")

shutil.copy("data.txt", "data_backup.txt")
print("backup exists:", os.path.exists("data_backup.txt"))

if os.path.exists("data.txt"):
    os.remove("data.txt")
    print("data.txt deleted")
else:
    print("data.txt not found")

print("data.txt exists:", os.path.exists("data.txt"))
