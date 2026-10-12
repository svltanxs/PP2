import re

print(re.sub(r"(?<!^)(?=[A-Z])", "_", input("Camel case: ")).lower())