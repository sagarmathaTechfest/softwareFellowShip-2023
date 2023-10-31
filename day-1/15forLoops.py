'''
For Loops

A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
'''

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


# Looping through a string

for x in "banana":
  print(x)

# break 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
# continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# range
for x in range(6): # range(6) is 0 to 5
  print(x)

#2 to 6
for x in range(2, 6):
  print(x)

# Else in for loops

for x in range(6):
  print(x)
else:
  print("Finally finished!")

# Nested For Loops

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)