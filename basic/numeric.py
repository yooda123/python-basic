# 数値型（Numeric）： integer, float, complex


# int
print(type(1))

# float (小数点を表す仕組み。誤差あり)
print(type(0.1))
print(0.1 + 0.1 + 0.1) # 0.3? -> 0.30000000000000004

# Numeric Operator(数値演算子)
print(1 + 0.4)
print(1 - 0.4)
print(2 * 3)
print(1 / 2) # float
print(5 * 6 - 3 / 6)
print(type(5 * 6 - 3 / 6))

result = 1 + 1.0 # floatになる
print(result)
print(f"type of result : {result} is {type(result)}")

# その他の演算
# floor division
print(14 // 3) # int 4
print(type(14 // 3)) 
print(14 / 3) # float 4.666666666666667
print(type(14 / 3))
# modulo, 剰余、余り
print(14 % 3)
# exponentiation, べき乗
print(2 ** 3)

hit_point = 100
attack_point = 40.3
remain = hit_point - attack_point
print(f"remain hit point is {remain}")


# augumented assignment +=, -=, *=, /=, //=
a = 1
a = a + 1
a += 1
print(a)