class Animal(object):
  def __init__(self, name) -> None:
      super().__init__()
      self.name = name
      print("Animal init is called.")

  def breath(self):
    print(f"{self.name} is breathing.")


class Dog(Animal):
  def __init__(self, name) -> None:
      super().__init__(name)
      print("Dog init is called.")

class Cat(Animal):
  pass


pochi = Dog("pochi")
tama = Cat("tama")

print(pochi.name)
print(tama.name)

pochi.breath()
tama.breath()