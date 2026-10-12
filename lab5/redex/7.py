import re

print(re.sub(r"_(\w)", lambda m: m[1].upper(), input("Snake case: ")))