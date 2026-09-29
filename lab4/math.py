import math
 
# 1. 
degree = float(input())
print("Output radian:", round(math.radians(degree), 6))
 
# 2. 
height = float(input())
base1 = float(input())
base2 = float(input())
print("Expected Output:", (base1 + base2) / 2 * height)
 
# 3. 
n = int(input())
side = float(input())
area = n * side ** 2 / (4 * math.tan(math.pi / n))
print("The area of the polygon is:", round(area, 2))
 
# 4. 
base = float(input())
h = float(input())
print("Expected Output:", base * h)
