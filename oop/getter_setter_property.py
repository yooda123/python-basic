from unicodedata import name


class Person:

  def __init__(self, name, age) -> None:
      self.name = name
      self._age = age # ★ここは必ず_age(アンダーバーつける。そうしないと無限ループになる)

  def get_age(self):
    print("get_age is called.")
    return self._age

  def set_age(self, age):
    print("set_age is called.")
    if age < 0:
      print("0以上の値を入れてください")
    else:
      self._age = age

  # age = property(get_age, set_age)  # ★ここは普通のage


john = Person('John', 10)
# print(john)
# print(john.get_age())
# # john.age = -10
# john.set_age(-20)
# print(john.get_age())

print(john.age)
john.age = -1