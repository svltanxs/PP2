import re

print(re.sub(r"(?<=\w)(?=[A-Z])", " ", input("String: ")))