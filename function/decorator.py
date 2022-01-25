# Decorator: 関数に機能を付属する（デコレートする）

def greeting(func):
  def inner(*args, **kwargs):
    print("Hello!")
    func(*args, **kwargs)
    print("Nice to meet you!")
  return inner

@greeting # say_name = greeting(say_name)
def say_name(name):
  print(f"I'm {name}.")

@greeting
def say_name_and_origin(name, origin):
  print(f"I'm {name}. I'm from {origin}.")
  
  
# 最初のsay_name()
# say_name(("Akiyo"))

# デコレートしたsay_name(9)
say_name(("Jiro"))
print("------------")
say_name_and_origin("Hana", "U.S.A")
print("------------")
say_name_and_origin(name="Taro", origin="Tokyo")
