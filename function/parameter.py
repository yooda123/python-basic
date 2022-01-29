def func(param1, param2, param3=1111111):
  print(f"first is {param1}, second is {param2}, third is {param3}.")

func('1', 32, ['a', 1, 2])

func('1', param3=['a', 1, 2], param2=32)

func('1', 32)