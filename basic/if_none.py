# ifでのNone
a = None
# a = 1
if a is None:
  print("a is None.")
else:
  print("a has value.")


if a:
  print("a has value.")
else:
  print("a is None.")


if not a:
  print("a is None.")
  a = 10
else:
  print("a has value.")
