fruits = ['apple', 'peach', 'grapes', 'banana']

for fruit in fruits:
  print(fruit)

for idx, fruit in enumerate(fruits):
  print(f"{idx}:{fruit}")

for x in enumerate(fruits):
  print(x) # tuple