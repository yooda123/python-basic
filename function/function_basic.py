# function(関数)
#print()
#len()
#input()

# 華氏から摂氏に変換する

def fahrenheit_to_celsius(fahrenheit):
  celsius = (fahrenheit - 32) * 5 / 9
  return celsius

fahrenheit = 72
celsius = fahrenheit_to_celsius(fahrenheit)
print(celsius)
