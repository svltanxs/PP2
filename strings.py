#upper case
a = "Hello, World!"
print(a.upper())

#lower case
a = "Hello, World!"
print(a.lower())

# remove whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# replace string 
a = "Hello, World!"
print(a.replace("H", "J"))

# split string 
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!'] 

# merge 
a = "hello"
b = "world"
print(a + b) # hello world

# f string function
age = 36
txt = f"My name is John, I am {age}"
print(txt)  

price = 59
txt = f"The price is {price} dollars"
print(txt)
#------------------------------------
x = "\'"      # Single Quote

x = "\\"      # Backslash

x = "\n"      # New Line

x = "\r"      # Carriage Return

x = "\t"      # Tab

x = "\b"      # Backspace

x = "\f"      # Form Feed

x = "\ooo"    # Octal Value

x = "\xhh"    # Hex Value

