#challenge
from audioop import add


games = {1: "ルーレット", 2: "ブラックジャック", 3: "ポーカー"}
add_games = {4: 'スロット'}
games.update(add_games)

age = int(input("あなたは何歳ですか？"))
if age >= 18:
  # ゲーム選択
  while True:
    for i, name in games.items():
      print(f"{i}: {name}")
    choice = int(input("ゲームを選択してください: "))

    if not choice in games.keys():
      print("\n!!!\n正しい選択肢を入力してください\n!!!\n")
    else:
      print(f"{games[choice]}をお楽しみください。")
      break
else:
  print("18歳未満は入場できません。")
