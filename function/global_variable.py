call_count = 0

CALL_COUNT = 0  # 定数（constant value)


def print_count1():
  global call_count
  call_count += 1

  print(f"関数1: {call_count}回目")

def print_count2():
  global call_count  # グローバル変数はなるべく使用しない、バグの元
  call_count += 1

  print(f"関数2: {call_count}回目")


print_count1()
print_count2()
