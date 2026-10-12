import re

found = re.search(r"[A-Z][a-z]+", input("String: "))
print("Found a match!" if found else "Not matched!")