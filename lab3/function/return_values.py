# return can be like that 
def function(x , y):
    return x
    return y
# it gives us only x and ignore y
def function(x , y):
    return x + y
# it gives us x + y

# recursion on python is like that it cals own function
def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))

