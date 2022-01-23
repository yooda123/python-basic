# mutable: 変更可能なオブジェクト list, dict, set
fruits = ['apple', 'peach', 'banana']
print(f"fruitのIDは{id(fruits)}")
fruits.append('lemon')
print(fruits)
print(f"fruitのIDは{id(fruits)}")


# immutable: 変更不可能なオブジェクト int, float, str, bool, tuple
fruit = 'apple'
print(f"fruitのIDは{id(fruit)}")
fruit += 'lemon'
print(fruit)
print(f"fruitのIDは{id(fruit)}")

# =================================================================
# メモリ非効率　→　文字列結合（＋）。文字列はimmutableなので毎回id変わる。
# =================================================================
text = "" # 1-2-3-4-5-6-..
for i in range(1, 11):
  if i == 1:
    text += str(i)
  else:
    text += "-" + str(i)
print(text)

# =================================================================
# メモリ効率良し　→　リストに文字列追加し、最後にjoin。リストはimmutableなのでidは常に同じ
# =================================================================
text_list = []
for i in range(1, 11):
  text_list.append(str(i))
print(text_list)
print("-".join(text_list))
