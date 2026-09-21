import math

def volume(radius):
    volume = (4 / 3) * math.pi * (radius ** 3)
    return volume
r = 5
print(f"Volume : {volume(r)}")