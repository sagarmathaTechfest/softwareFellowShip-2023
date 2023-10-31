'''
If Else (comparision)


Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
'''

a = 33
b = 200
if b > a:
  print("b is greater than a") # be sure to check your intendation


# using Elif

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# using Else
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#short hand 

if a > b: print("a is greater than b")

a = 2
b = 330
print("A") if a > b else print("B") # shorthand else
print("A") if a > b else print("=") if a == b else print("B")

# using logical operators

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")


a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

# nested If

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# pass - if you have nothing to do

a = 33
b = 200

if b > a:
  pass