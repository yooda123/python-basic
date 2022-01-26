def myfunc():
  print("This is my function!")

myvariable = "This is global variable."

def anotherfunc():
  print("This is another function!!")

def _non_public_func(): # 外からアクセスしない意思表示（実際はアクセスはできる）
  print("non public func")

if __name__ == "__main__": # 外からインポートされたら"mymodule"になるのでprintは実行されない
  myfunc()
  anotherfunc()
  _non_public_func()
  print("This is mymodule!!")
  # print(f"mymodule.__name__: {__name__}")
