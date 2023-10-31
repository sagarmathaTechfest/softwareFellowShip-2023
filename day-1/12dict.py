'''
Dictionary

Dictionaries are used to store data values in key:value pairs.
- ordered - used to be unordered (3.6 and before)
- changeable 
- does not allow duplicate values.
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

print(thisdict["brand"]) # accessing using a key
x = thisdict.get("model") # using .get() method
x = thisdict.keys() # List all the key of the dict
x = thisdict.values() # List all the values of the dict
x = thisdict.items() # converts the key:value into tuples in a list


# multiple data types in a dict

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(type(thisdict))

# dict constructor

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

# Check if a key exists or not

print("model" in thisdict)

# Change values

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

# Change values using update method

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

# Add a new key:value

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

# Add a new key:value using update

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

# Removing a key:value using pop

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

# popitem removes the last key:val

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

# using del to remove element

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

# clearing a list 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

# deleting a list

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
# print(thisdict) #this will cause an error because "thisdict" no longer exists.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Loop in a dict

for x in thisdict:
  print(x)

# print values
for x in thisdict:
  print(x, ':', thisdict[x])

# Loop through key and values

for x, y in thisdict.items():
  print(x, y)

# copying a dict
# using copy
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# using dict()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

# Nested Dict

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}


myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : {
  "name" : "Linus",
  "year" : 2011
}
}

print(myfamily["child2"]["name"])