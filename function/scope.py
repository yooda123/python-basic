def print_name_local():
  # ローカル変数
  first_name = "Taro"
  last_name = "Yamada"
  print(f"I'm {first_name} {last_name}.")

print_name_local()  

# グローバル変数（モジュール変数）
age = 30

def print_age():
  global age
  age = 20 # グローバル変数を上書き
  print(f"I'm {age} years old.")

print_age()
print(age)