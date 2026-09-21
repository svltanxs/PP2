#lambda its a mini function that don't required to call with def
x = lambda a : a + 10
print(x(5))
# and it can be like that or more
x = lambda a, b : a * b
print(x(5, 6)) 
# this one is crazy we can call function and after we can change the value of lambda
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))
#it triples the number for example 11 become 33 if we put 4 instead of 3 it would give 44
