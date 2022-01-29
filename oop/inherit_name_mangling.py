class Person:
  def __init__(self, name) -> None:
      self.name = name
      self.__mymethod()

  def mymethod(self):
    print("Person method is called.")

  __mymethod = mymethod


class Baby(Person):
  def mymethod(self):
    print("Baby method is called.")


taro_baby = Baby("Taro")
print(taro_baby.name)
taro_baby.mymethod()

taro_person = Person("Taro")
# taro_person._Person__mymethod()
taro_person.mymethod()