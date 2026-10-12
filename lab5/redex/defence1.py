
def evenn(x):
    if(x % 2 == 0):
        yield x
    
n = int(input())
for i in range(n):
    
    print(*evenn(i))

