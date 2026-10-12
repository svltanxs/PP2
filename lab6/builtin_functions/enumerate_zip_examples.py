names = ["Ali", "Dana", "Timur"]
ages = [18, 19, 20]

for i, name in enumerate(names):
    print(i, name)

for i, name in enumerate(names, start=1):
    print(i, name)

for name, age in zip(names, ages):
    print(name, age)

print(dict(zip(names, ages)))
