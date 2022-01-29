# 関数の中で関数を定義（nested function）

msg = "I am global."

def outer(outer_param):
  msg = "I am outer."
  def inner():
    inner_variable = "Inner var"
    # nonlocal msg
    # msg = "I am inner."

    print("This is inner function.")
    print(outer_param)  # アウター関数のローカル変数はインナーで利用できる。上書きはglobal or nonlocalとする
    print(msg)

  inner()
  print("This is outer function.")
  print(msg)
  # print(inner_variable)         # インナー関数のローカル変数はアウターで利用できない

outer("outer arg")
# inner()
print(msg)
