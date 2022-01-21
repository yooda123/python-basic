# if
age = 20
age_alcohol = 21

if age >= age_alcohol:
  print("You can drink beer.")
else:
  print("You are too young to drink beer")


if age >= age_alcohol:
  print("You can drink beer.")
elif age >= 10:
  print("You are too young to drink beer")
else:
  print("others")