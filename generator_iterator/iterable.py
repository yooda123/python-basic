fruits = ['apple', 'lemon', 'peach']

# next(fruits)
fruit_iterator = iter(fruits)
# print(next(fruit_iterator))
print(id(fruit_iterator))
print(id(iter(fruit_iterator)))


print(next(fruit_iterator))
print(fruit_iterator.__next__())
