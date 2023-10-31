'''
While Loops

Execute as long as the condition is true
'''
i = 1
while i < 6:
  print(i)
  i += 1

# stopping a loop: break

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


# skip a loop

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# we can run a block of code once when the condition no longer is true:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")