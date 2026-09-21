def reverse_s(sentence):
    words = sentence.split()
    result = ""
    for i in range(len(words) - 1, -1, -1):
        result = result + words[i]
        if i != 0:
            result = result + " "
    return result


sentence = input()
result = reverse_s(sentence)
print(result)