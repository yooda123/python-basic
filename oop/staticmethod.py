class MyClass:
  
  classmethod_count = 0

  def mymethod(self):
    print("This is normal method.")

  @staticmethod
  def mystaticmethod():
    print("This is staticmethod.")

  @classmethod
  def myclassmethod(cls):
    cls.classmethod_count += 1
    print(f"This is classmethod and now the count is {cls.classmethod_count}")

if __name__ == '__main__':
  c = MyClass()
  c.mymethod()
  MyClass.mystaticmethod()
  MyClass.myclassmethod()
  MyClass.myclassmethod()