# リスト（lists）：複数のオブジェクトを順序付けて保存するデータ型
# []で括って、,(カンマ)で各オブジェクトを区切る
fruits = ['apple', 'peach', 'melon', 'grapes']

hetro_list = ["string", 1, 3.4, True, fruits]

print(hetro_list)
print(fruits[1])
print(fruits[-2]) # melon
print(hetro_list[-1][-2]) # melon

print("hello world"[-3])
print("hello world"[5])

print(fruits)
# .append(): 新しいオブジェクトを追加する
fruits.append('banana')
print(fruits)
# .insert(): 指定したindexに指定したオブジェクトを追加する
fruits.insert(3, 'lemon')
print(fruits)
# .remove(): マッチした最初のオブジェクトを除く
fruits.remove('peach')
print(fruits)
# .sort(): 昇順, 降順に並び替える
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
# .len(): リストの要素数を取得、文字列の長さもわかる
print(len(fruits))
print(len("Hello world!"))
