# from dis import show_code
import time

class Account(object):
  count = 0

  def __init__(self, balance, name) -> None:
    super().__init__()
    self.balance = balance
    self.name = name
    self.transaction = []
    self.account_number = Account.count
    Account.count += 1
    print("口座を作成しました。口座名:{0.name} 口座番号:{0.account_number} 残高:{0.balance}".format(self))


  def deposit(self, amount):
    self.balance += amount
    self.make_transaction(amount, Account.getDateTime())
    self.show_balance()


  def withdraw(self, amount):
    if self.balance < amount:
      print("残高が足りません。")
    else:
      self.balance -= amount
      self.make_transaction(amount * -1, Account.getDateTime())
      self.show_balance()

  def show_balance(self):
    print("口座名:{0.name} 口座番号:{0.account_number} 残高:{0.balance}".format(self))

  def make_transaction(self, amount, time):
    self.transaction.append({'amount': amount, 'balance': self.balance, 'datetime': time})

  def show_transaction(self):
    print("------------------------------")
    print(f"{self.name}さんの取引情報")
    print("------------------------------")
    print("日時 取引金額 残高")
    for tr in self.transaction:
      # print(f"{tr['datetime']} {tr['amount']} {tr['balance']}")
      tr_str_list = []
      for k, v in tr.items():
        tr_str_list.append(f"{k}: {v}")
      print(", ".join(tr_str_list))

  @staticmethod
  def getDateTime():
    localtime = time.localtime()
    now = "{0.tm_year}/{0.tm_mon}/{0.tm_mday} {0.tm_hour}:{0.tm_min}:{0.tm_sec}".format(localtime)
    return now




if __name__ == '__main__':
  taro = Account(balance=1000, name='TARO KUBOTA')
  nana = Account(500, 'NANA YAMAKAWA')

  taro.deposit(1)
  time.sleep(1)
  nana.deposit(300)
  time.sleep(1)

  taro.withdraw(1002)
  time.sleep(1)
  nana.withdraw(801)
  time.sleep(1)

  taro.withdraw(1001)
  time.sleep(1)
  nana.withdraw(800)
  time.sleep(1)

  taro.show_transaction()
  nana.show_transaction()