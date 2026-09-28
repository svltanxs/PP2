def spy_game(nums):
    index = 0
    code = [0, 0, 7]
    for i in range(len(nums)):
        if nums[i] == code[index]:
            index = index + 1
            if index == len(code):
                return True
    return False


print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # False