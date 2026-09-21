def ch_palindrome(str):
    cnt = 0
    for i in range(len(str) // 2):
        if(str[i] == str[len(str) - i - 1]):
            cnt+=1
    if(cnt == len(str) // 2):
        print("YES")
    else:
        print("NO")
str = input()
ch_palindrome(str)
# 0 1 2 3 4 3 2 1 0