'''
Tuples
Tuples are used to store multiple items in a single variable.

- ordered
- unchangeable 
- allow duplicate values.
'''


mytuple = ("apple", "banana", "cherry") # This is a tuple

thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Allows duplicate

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Len of a tuple

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# we can use any data types in a tuple

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(type(tuple1))

# Tuple constructor

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

# Accessing Tuples

thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) # Normal Indexing

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1]) # Negative Indexing

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5]) # Index range

# Indexing from the start

# Indexing to the end

# Negative Indexing range

# Changing Tupple values

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# same as the list

#unpacking tuples

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# another type of unpacking

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#Iterating in tuples

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])


# Joining two tuples

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# Multiplying

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)