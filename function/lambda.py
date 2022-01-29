# lambda関数（無名関数）

def square(x):
  return x * x

print(square(3))

s = lambda x: x * x
print(s(3))


# def power(exponent):
#   def inner_power(base):
#     return base ** exponent
#   return inner_power

def power(exponent):
  return lambda base: base ** exponent

third_power = power(3)
print(third_power(5))

numbers = [6, 2, 5, 43, 5, 36, 67, 2]
filterd_num = filter(lambda x: x % 2, numbers) # lambda x: x % 2 == 1(True)
print(list(filterd_num))
