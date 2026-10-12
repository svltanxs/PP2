import re

found = re.fullmatch(r"[a-z]+_[a-z]+", input("String: "))
print("Found a match!" if found else "Not matched!")