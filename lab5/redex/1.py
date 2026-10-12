import re
 
found = re.search(r"ab*", input("String: "))
print("Found a match!" if found else "Not matched!")
 
