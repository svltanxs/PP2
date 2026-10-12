import re

found = re.search(r"a.*b$", input("String: "))
print("Found a match!" if found else "Not matched!")