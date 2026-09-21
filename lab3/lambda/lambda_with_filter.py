# filter its receive two parametrs first one is boolean and if its true we get the number
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

# or we have alternative code like that
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = [x for x in numbers if x % 2 != 0]
print(odd_numbers)
