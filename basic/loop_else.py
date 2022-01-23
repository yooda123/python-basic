fruits = ['apple', 'peach', 'grapes', 'banana']

for fruit in fruits:
  choice = input(f"あなたが探しているフルーツは{fruit}ですか？ y/n:")
  if choice == 'y':
    print("見つかってよかったですね")
    break
  else:
    print("そうですか。。")

  print(fruit)
else:
  print('お探しのフルーツは見つかりませんでした。')

# while else
count = 0
while count < 10:
  print(count)
  count += 1
else:
  print("countは10未満ではなくなりました")


balance = 1000
game_price = 200
while game_price <= balance:
  choice = input(f"1回{game_price}円です。プレイしますか？（残高{balance}円） y/n:")
  if choice == 'y':
    balance -= game_price
    print(f"楽しんでください。")
    continue
  elif choice == 'n':
    print("ゲームを終了します。お疲れさまでした。")
    break
  else:
    print("yかnを入力してください。")
else:
  print("残高が足りないので、ゲームを終了します。")