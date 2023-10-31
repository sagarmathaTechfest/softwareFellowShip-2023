'''
used to convert one data type to another
Also called Type Casting

Two Types: 
1. Implicit Type Casting
2. Explicit Type Casting
'''

# Example Implicit Type Casting

x = 12
y = 12.0
z = x + y
print(z)

# Example Explicit Type Casting

x = 12
y = '12'
z = x + int(y)
print(z)

# More example

a = 12
print('numeric a',a)
print("Type casting 'a' to float", float(a))
print("Type casting 'a' to string", str(a))


b = 12.35
