# 再起関数（recursive function）: 関数内で自分の関数をcallする
# 階乗(factorical): 3! = 3 * 2 * 1 = 6
# n! = n * (n-1) * (n-2) * ... * 1
# n! = n * (n-1)!


def factorical(n):
  if n == 1:
    return 1
  return n * factorical(n - 1)

print(factorical(3))


# challenge1: 再帰バージョン　→　★遅い！！★
def fibonacci_recursive(n):
  if n < 2:
    return n
  return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

print(fibonacci_recursive(35))

# challenge2: 再帰なしバージョン
def fibonacci_nonrecusive(n):
  if n < 2:
    return n
  n_1 = 1
  n_2 = 0
  for _ in range(n-1):
    result = n_2 + n_1
    n_2 = n_1
    n_1 = result
  return result

print(fibonacci_nonrecusive(35))
