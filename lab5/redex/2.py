import re

found = re.search(r"ab{2,3}", input("String: "))
print("Found a match!" if found else "Not matched!")