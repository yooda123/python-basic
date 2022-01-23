# range(start, stop, step)
for i in range(1, 7, 1):
  print(i)

for i in range(1, 7):
  print(i)

for i in range(0, 7, 2):
  print(i)

for i in range(10):
  print("hello")

# challenge
for i in range(1,51):
  if i % 15 == 0:
    print(f"FizzBuzz")  
  elif i % 5 == 0:
    print(f"Buzz")  
  elif i % 3 == 0:
    print(f"Fizz")
  else:
    print(i)