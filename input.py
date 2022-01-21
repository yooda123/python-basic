# input(): ユーザの入力した値（文字列）を取得
age = input("何歳ですか？")
print(f"{age}歳です！")

if int(age) >= 18:
  # カジノ作成
  message = ("""
  カジノへようこそ。
  どちらをプレイしますか。
  1 : ルーレット
  2 : ブラックジャック
  3 : ポーカー
  """)
  select = input(message)
  if int(select) == 1:
    print("ルーレットを楽しんでください！！")
  elif int(select) == 2:
    print("ブラックジャックを楽しんでください！！")
  elif int(select) == 3:
    print("ポーカーを楽しんでください！！")
  else:
    print("1～3を選んでください")

else:
  print("18歳未満の人はカジノへ入れません")
