# Type Annotation 
def add_nums(num1: int, num2: int) -> int:
  return num1 + num2

print(add_nums(1,2)) # ok
print(add_nums("1","2")) # ok

# pythonは動的型付け
# type annotationはpythonの思想と異なるので
# 現場で使うことは少ない