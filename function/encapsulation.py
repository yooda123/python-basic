# カプセル化（encapsulation）：外からアクセスできないようにする

def casion_entrance(age, min_age=21):
  if age < min_age:
    print(f"{min_age}未満はお断り")
    return

  def inner_casino_entrance():
    print("ようこそカジノへ")

  return inner_casino_entrance()


# inner_casino_entrance()
casion_entrance(28)