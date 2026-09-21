def unique_elements(lst):
    result = []
    for item in lst:
        if (item not in result):
                result.append(item)
    return result
print(unique_elements([1, 2, 2, 3, 1, 4, 3]))
