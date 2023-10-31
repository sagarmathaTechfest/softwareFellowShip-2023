'''
List
Lists are used to store multiple items in a single variable.

Properties
- ordered
- changeable 
- allow duplicate values.
'''

thisList = ["apple", "banana", "cherry"]
print(thisList)
print(type(thisList))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

list4 = ["abc", 34, True, 40, "male"]

# List constructor - Ctreating list another way
listConstructor = list(("apple", "banana", "cherry")) # note the double round-brackets

# Accessing Items

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1]) # Normal Indexing

print(thislist[-1]) # Negative Indexing

print(thislist[2:5]) # Range of Indexes

print(thislist[-4:-1]) # Range of Negative Indexes


# Check if Item Exists
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# Change Item Value

thislist[1] = "blackcurrant"
print(thislist)

# Change a Range of Item Values

thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Insert Items

thislist.insert(2, "watermelon")
print(thislist)

# Append Items - Adds item to the end of the list

thislist.append("orange")
print(thislist)

# Insert Items - Inserts item to the specified position

thislist.insert(1, "orange")
print(thislist)


# Extend List - Add elements of another list

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Join list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Remove List Items

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]

thislist.remove("banana") # only removes first occurance
print(thislist)

thislist.pop(1) # Remove Specified Index
print(thislist)

thislist.pop(0) # Remove last element
print(thislist)

# Remove element using del
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) # it will not print anything

del thislist # removes entire list

# clear list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) # makes the list empty


# Iterating through the list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# range
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


# Sorting
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

thislist.reverse() # reverse the elements
print(thislist)

# Copying a list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
mylist2=list()
mylist2=thislist

print(mylist)

thislist[1]="cat"
print(thislist)
print(mylist)
print(mylist2)