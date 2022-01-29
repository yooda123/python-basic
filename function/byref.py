# 参照渡し（byref） <-> 値渡し（byvalue）
# def add_nums(a, b):
#   print(f"a: {id(a)}, b: {id(b)}")
#   a = 100
#   print(f"a: {id(a)}, b: {id(b)}")

#   return a + b

# one = 1
# two = 2

# print(f"one: {id(one)}, two: {id(two)}")
# print(add_nums(one, two))
# print(f"one: {id(one)}, two: {id(two)}")

def add_one(num):
  print(f"変更前のID: {id(num)}")
  num += 1
  print(f"変更後のID: {id(num)}")
  return num

one = 1
print(f"変更前のID: {id(one)}")
print(add_one(one))
print(f"変更後のID: {id(one)}") 
print(one) # immutableなオブジェクトだと値は変わらない
print("################################")

def add_fruit(fruits, fruit):
  print(f"変更前のID: {id(fruits)}")
  fruits.append(fruit)
  print(f"変更後のID: {id(fruits)}")

fruits = ['apple', 'banana']
print(fruits)
print(f"呼出前のID: {id(fruits)}")
add_fruit(fruits, 'peach')
print(f"呼出後のID: {id(fruits)}") 
print(fruits) # mutableなオブジェクトだと値が変わる  -> list, dict, set