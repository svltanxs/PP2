x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)
# += -= operators
x = 5          # =
x += 3         # x = x + 3
x -= 3         # x = x - 3
x *= 3         # x = x * 3
x /= 3         # x = x / 3
x %= 3         # x = x % 3
x //= 3        # x = x // 3
x **= 3        # x = x ** 3
x &= 3         # x = x & 3
x |= 3         # x = x | 3
x ^= 3         # x = x ^ 3
x >>= 3        # x = x >> 3
x <<= 3        # x = x << 3
print(x := 3)  # x = 3, print(x)

# ternary operators
num = 6

x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"

print(x)

# in, not in
text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)
