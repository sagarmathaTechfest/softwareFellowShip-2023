'''
Sets
Sets are used to store multiple items in a single variable.

- unordered
- unchangeable but remove and add can be done
- does not allow duplicate values.
'''

thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)


set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"} # any data types can be inserted

print(type(set4))

# Constructor for sets
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

# Accessing - only through iterations because it is unordered

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# but we can check if a element is present or not
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

# Adding items

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# Adding sets

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# Adding any iterables

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

# removing elements

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

# removing elements using discard

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

# removing element using pop - it will remove a random element

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

# clearing a set 

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

# deleting the set 

thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

# Looping in sets

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


# joining two sets

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# keeping only the duplicates

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

# keeping only the duplicates 

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

# Keep All, But NOT the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

# True and 1 is considered the same value:

x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)

print(z)