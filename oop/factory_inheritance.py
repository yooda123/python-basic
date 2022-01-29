import time

class Person:

  def __init__(self, name, age) -> None:
      # pass
      self.name = name
      self.age = age

  # ファクトリー(例えば誕生日を引数で受け取り、誕生日から年齢を算出してインスタンス生成)
  @classmethod
  def create_from_birth(cls, name, year, month, date):
    today = time.localtime()
    age = today.tm_year - year - ((today.tm_mon, today.tm_mday) < (month, date))
    return cls(name=name, age=age)

  @staticmethod
  def create_from_birth2(name, year, month, date):
    today = time.localtime()
    age = today.tm_year - year - ((today.tm_mon, today.tm_mday) < (month, date))
    return Person(name=name, age=age)


class Baby(Person):
  pass

# john = Person('John', 30)
#john = Person.create_from_birth('John', 1980, 1, 27)
john = Baby.create_from_birth('John', 1980, 1, 27)
print(type(john))# Babyクラス
print(f"name: {john.name}, age: {john.age}")

# emma = Person.create_from_birth('Emma', 1989, 4, 3)
emma = Baby.create_from_birth('Emma', 1989, 4, 3)
print(type(emma)) # Babyクラス
print(emma.name)
print(emma.age)

# emily = Person.create_from_birth2('Emily', 1999, 12, 3)
emily = Baby.create_from_birth2('Emily', 1999, 12, 3)
print(type(emily)) ### ★★ Personクラス！？ staticmethod使っているから
print(emily.name)
print(emily.age)
