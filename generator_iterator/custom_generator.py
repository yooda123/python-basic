# range(10)

from ast import Num


def myrange(stop):
    start = 0
    while start < stop:
        yield start
        start += 1


mr = myrange(10)
# print(type(mr))  # <class 'generator'>
# print(mr)  # <generator object myrange at 0x000002580D159E70>

print(next(mr))
print(next(mr))
print(next(mr))

for i in mr:
    print(':' + str(i))

# print(next(mr)) # StopIteration例外

print("=" * 30)
print("challenge 1")

# challenge1


def even(num):
    while num != 0:
        if num % 2 == 0:
            yield num
        num -= 1


print("=" * 30)
for i in even(10):
    print(i)

print("=" * 30)
even_gen = even(10)
print(next(even_gen))
print(next(even_gen))

print(id(iter(even_gen)))
print(id(even_gen))
