# in演算子
fruits = ['apple', 'peach', 'grapes', 'banana']
print('apple' in fruits)
print('lemon' not in fruits)

print('H' in "Hello")


#challenge
favorite_fruit = input('好きなフルーツを入力してください\n')
if favorite_fruit in fruits:
  print(f"{favorite_fruit}ですね。差し上げます。")
  fruits.remove(favorite_fruit)
elif favorite_fruit != '':
  print(f"{favorite_fruit}ですね。仕入れました。")
  fruits.append(favorite_fruit)
  
print(f"今あるフルーツはこちらです。\n{fruits}")