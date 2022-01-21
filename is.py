# is演算子: 同じオブジェクトかどうか判定する
a = 1
b = 1
c = 3
d = 1
e = 2 - 1 # 1
f = a
print(a is b is d) # True
print(a is b is c) # False
print(id(a))
print(id(b))
print(id(1))

print(a is not c) # True
print(a is e) # True
print(a is f) # True

hello = "hello"
hello2 = "h" + "e" + "l" + "l" + "o" # "hello"
print(hello, hello2)
print(hello is hello2) # True
hello = "konnichiwa"
print(hello is hello2) # False

# Noneかどうかの判定によく使う
nothing = None
print(nothing)
print(nothing is None)
print(id(nothing))
print(id(None))