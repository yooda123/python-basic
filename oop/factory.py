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



# john = Person('John', 30)
john = Person.create_from_birth('John', 1980, 1, 27)
print(f"name: {john.name}, age: {john.age}")