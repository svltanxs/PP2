mylist = ["apple", "banana", "cherry"]


# type()
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# slicing list
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#changing 
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# append adds element to the back
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# insert adds element where you want
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# remove() delete first matched element
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# pop delete last one
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# del function
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#loop through list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) 

# loop through the index
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i]) 

#sort list
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#desc sort
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# copy list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#