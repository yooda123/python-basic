# 「:」を使って、複数の要素をとってくることができる（slincing）
even = [2, 4, 6, 8, 10, 12]
# 基本は[開始:未満]
print(even[1:4])

print(even[0:4])
print(even[:4])
print(even[3:])
print(even[3:5])
print(even[-3:-1])

text = "hello world"
print(text[3:])

# [開始:未満:step]
print(text[2:10:2])
print(text[::-1])
#print(text.sort(reverse=True)) #文字列にはsort使えない