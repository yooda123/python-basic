# tuple（タプル）：変更できないリスト []ではなく()を使う
date_of_birth = [1999, 2, 3]
date_of_birth[0] = 2000
print(date_of_birth)

date_of_birth = (1999, 2, 3)
# date_of_birth[0] = 2000
print(date_of_birth[0])

year, month, day = date_of_birth
print(f"{year}年{month}月{day}日")
