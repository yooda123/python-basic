class Person:
# class Person(object):のこと

  num_legs = 2

  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

  def walk(self):
    print(f"{self.name} is walking.")

  def run(self):
    print(f"{self.name} is running.")


john = Person("John", 28, "male")
taro = Person("Taro", 18, "male")
emma = Person("Emma", 40, "female")

# インスタンス変数
print(john.name)
john.age = 29
print(john.age)
print(john.gender)

print(taro.name)
print(taro.age)
print(taro.gender)

print(emma.name)
print(emma.age)
print(emma.gender)

# インスタンスメソッド
john.walk()
taro.walk()
emma.walk()
john.run()

print(john.num_legs)
print(taro.num_legs)
print(emma.num_legs)

Person.num_legs = 10

print(john.num_legs)
print(taro.num_legs)
print(emma.num_legs)

taro.num_legs = 1

print(john.num_legs)
print(taro.num_legs)
print(emma.num_legs)

# from car import *

# prius = Car("prius", 22, "TOYOTA")
# prius.gas()

# import car
# prius = car.Car('a', 1, 'BBB')

# from car import Car
# prius = Car("aaa")
