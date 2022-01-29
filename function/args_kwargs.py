#########
# *args
#########
#print("Hello", "World", "test")

def get_averate(*num): # tupleで受け取る
  if (len(num)) == 0:
    return 0
  total = sum(num)
  return total / len(num)

print(get_averate())
print(get_averate(1, 2, 3))

#########
# *kwargs
#########
def kwargs_func(**kwargs):
  print(kwargs)
  param1 = kwargs.get('param1', 1)
  param2 = kwargs.get('param2', 2)
  param3 = kwargs.get('param3', 3)

  print(f"param1: {param1}, param2: {param2}, param3: {param3}")

kwargs_func(param1=10, param2=6, param3=100, param4=500)


# * と ** はunpacking operator
numbers = (1, 2, 3)
print(numbers)
print(*numbers)
print(1, 2, 3)

a = {'a': 1, 'b': 2}
b = {'c': 3, 'd': 4}
c = {**a, **b}
print(c)