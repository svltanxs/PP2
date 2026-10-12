import os

os.makedirs("letters", exist_ok=True)

for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    with open("letters/" + letter + ".txt", "w") as f:
        f.write(letter)

print(os.listdir("letters"))
