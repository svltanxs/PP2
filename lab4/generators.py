# 1
N = int(input())
sq = (x*x for x in range(N+1))

for i in sq:
    print(i)

# 2
n = int(input())
ls = (x for x in range(n+1) if x % 2 == 0)

for i in ls:
    print(i, end=",")

# 3
def even_numbers(n):
    for i in range(n+1):
        if (i % 3 == 0 and i % 4 == 0):
            yield i

n = int(input())

for x in even_numbers(n):
    print(x)

# 4
def squares(a, b):
    for i in range(a, b+1):
        yield i*i

a, b = map(int,input().split())
for i in squares(a, b):
    print(i)

# 5
n = int(input())
ls = (x for x in range(n, -1, -1))
for i in ls:
    print(i)