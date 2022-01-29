from functools import lru_cache
import time

# .time(): 1970/1/1 秒数が表示 (Unix時間)
print(time.time())
print(time.time()/(60*60*24*365))


@lru_cache
def fib(n):
  if n < 2:
    return n
  else:
    return fib(n-1) + fib(n-2)

before = time.time()
# 処理
print(fib(40))
after = time.time()
print(f"{after - before:.2f} sec")

# .ctime() 今のローカル時間を文字列で返す
print(time.ctime())

# .localtime() 構造化データで返す
localtime = time.localtime()
print(localtime)
print(localtime.tm_year)

# .sleep(secs) secs秒だけプログラムが待機する
sec = 10
print(f"{sec}秒だけ待ってください")
# time.sleep(sec)
print(f"{sec}秒経ちました")


def timer(func):
  def inner(*args, **kwargs):
    before = time.time()
    func(*args, **kwargs)
    after = time.time()
    print(f"{func.__name__} tooks {after - before:.2f} sec.")
  return inner

@timer
def lazy_func(sec):
  print(f"I'm working so hard...")
  time.sleep(sec)
  print(f"I'm finally done!!")

lazy_func(4)