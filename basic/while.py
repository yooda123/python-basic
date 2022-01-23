# whileループ
count = 0
while count < 10:
  print(count)
  count += 1

# break, continue
while True:
  age = int(input("あなたは何歳ですか？"))
  if not 0 <= age < 120:
    print("入力された値は正しくありません。")
    continue
  else:
    print(f"あなたは{age}歳です。")
    break

#challenge
games = ["ルーレット", "ブラックジャック", "ポーカー"]
age = int(input("あなたは何歳ですか？"))
if age >= 18:
  # ゲーム選択
  while True:
    print(f"""
      1: {games[0]}
      2: {games[1]}
      3: {games[2]}
    """)
    game = int(input("ゲームを選択してください"))
    if not 1 <= game <= 3:
      print("1から3を入力してください")
      continue
    else:
      print(f"{games[game - 1]}をお楽しみください。")
      break
else:
  print("18歳未満は入場できません。")