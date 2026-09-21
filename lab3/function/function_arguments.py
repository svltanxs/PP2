# we can add parametres on function and we do like that 
def student(name,lastname,id,number,age,sex):
    print("Student name:" , name ,"\n")
    print("Student lastname:" , lastname ,"\n")
    print("Student id:" , id ,"\n")
    print("Student number:" , number ,"\n")
    print("Student age:" , age ,"\n")
    print("Student sex:" , sex , "\n")
student("Beka" , "Nurik" , "12adf5" , 8787, 18, "male")
# and we can do like that if parametr are empty we can use another one
def my_function(country = "Norway"):
  print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil") 
# it woud give us like that 
#I am from Sweden
#I am from India
#I am from Norway
#I am from Brazil 

# and we can switch order using keywords like that 
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog") 
# we see that animal its first and name is second but we swap it like that

# (, /) it means that we need to write like order we cant write like that
def my_function(name, /):
  print("Hello", name) # its wrong
my_function(name = "Emil") 

# and opposite (*,) it means we need to write key word
def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil") 
