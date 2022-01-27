class MyClass(object):
  def __str__(self):
    # return super().__str__()
    return "MyClassの__str__"



mc = MyClass()
print(mc) # mc.__str__()
print(1) # 1.__str__()
print("1")
print(True)
print([1, 2, 3])


various_types = [1, "1", True, [1,2,3], (1,), {'1': 1}, {1}]
for elem in various_types:
  print(elem)


def printvalue(arg):
  print(arg + 1)

printvalue(1)
printvalue(True)
# printvalue("1") # Error!