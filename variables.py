a = 4
A = "Sally"
#A will not overwrite a 

#----------------------------------------
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#----------------------------------------
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
#----------------------------------------
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 
#----------------------------------------