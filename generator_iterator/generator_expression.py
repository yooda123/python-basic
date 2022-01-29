import sys

square_list = [num * num for num in range(1000)]
print(square_list)

square_gen = (num * num for num in range(1000))
print(next(square_gen))
print(next(square_gen))
print(next(square_gen))
print(next(square_gen))

print(sys.getsizeof(square_list))
print(sys.getsizeof(square_gen))


even_squares = [num * num for num in range(10) if num % 2 == 0]
print(even_squares)

even_squares_gen = (num * num for num in range(10) if num % 2 == 0)
for num in even_squares_gen:
    print(num)
