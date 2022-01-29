class Account:

  def __init__(self, balance) -> None:
      self.__balance = balance

  def deposit(self, amount):
    self.__balance += amount
    self.show_balance()

  def withdraw(self, amount):
    if self.__balance < amount:
      print("残高が足りません")
    else:
      self.__balance -= amount
      self.show_balance()

  def show_balance(self):
    print(f"残高は{self.__balance}です")

myaccount = Account(5000)
# myaccount.deposit(1000)
# myaccount.withdraw(3000)
# myaccount.__balance = 1000
# print(myaccount.__balance)

print(dir(myaccount))
###
#__balance（アンダースコア2つ）にすると、'_Account__balance'が出現する  →名前修飾（name_mangling）
###
# ['_Account__balance', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'deposit', 'show_balance', 'withdraw'] 

myaccount.deposit(1000)
myaccount.withdraw(10000)
myaccount.__balance = -1000000
print(myaccount.__balance)
myaccount.show_balance()
print(dir(myaccount))
