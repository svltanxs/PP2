from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = list(map(lambda x: x * x, numbers))
print(squares)

even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)

total = reduce(lambda a, b: a + b, numbers)
print(total)

product = reduce(lambda a, b: a * b, numbers)
print(product)

print(len(numbers))
print(sum(numbers))
print(min(numbers))
print(max(numbers))
print(sorted([5, 2, 9, 1]))
print(sorted([5, 2, 9, 1], reverse=True))
