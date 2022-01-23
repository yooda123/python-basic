# dictionary: キーと値の組合せを複数保持するデータ型
fruits_colors = {'apple':'red', 'lemon':'yellow', 'grapes':'purple'}
print(fruits_colors)
print(fruits_colors['apple'])

fruits_colors['peach'] = 'pink'
print(fruits_colors)

dict_sample = {1: 'one', 'two': 2, 'three':[1, 2, 3], 'four': {'inner': 'dict'}}
print(dict_sample)
print(dict_sample['four']['inner']) 

colors = {}
colors['1'] = 'blue'
colors['0'] = 'red'
colors['2'] = 'green'
print(colors)

# .keys(), .values()
print(fruits_colors.keys())
for fruit in fruits_colors.keys():
  print(fruit)

print(fruits_colors.values())
for color in fruits_colors.values():
  print(color)

# .items()
print(fruits_colors.items())
for fruit, color in fruits_colors.items():
  print(f"{fruit}:{color}")