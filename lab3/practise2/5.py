def permutations(s):
    if len(s) <= 1:
        return [s]
    
    result = []
    for i in range(len(s)):
        first = s[i]
        rest = s[:i] + s[i+1:]
        for p in permutations(rest):
            result.append(first + p)
    return result


string = input()
all_perms = permutations(string)

for p in all_perms:
    print(p)