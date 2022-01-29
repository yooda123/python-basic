# Iteratorは、__next__()と__iter__()を持っている

class MyIterator:
    def __init__(self, start) -> None:
        self.current = start

    def __next__(self):
        num = self.current
        self.current += 1
        return num

    def __iter__(self):
        return self


myiterator = MyIterator(10)
print(next(myiterator))
print(next(myiterator))
print(next(myiterator))

print(id(iter(myiterator)))
print(id(myiterator))

print("=" * 30)
print("challenge 1")
print("=" * 30)


class EvenIterator:
    def __init__(self, num) -> None:
        self.current = num

    def __next__(self):
        if self.current < 2:
            raise StopIteration
        elif self.current % 2 == 0:
            num = self.current
            self.current -= 2
            return num
        else:
            self.current -= 1
            return self.__next__()

    def __iter__(self):
        return self


if __name__ == '__main__':
    evenIter = EvenIterator(10)
    print(id(iter(evenIter)))
    print(id(evenIter))

    print(next(evenIter))
    print(next(evenIter))
    print(next(evenIter))
    print(next(evenIter))
    print(next(evenIter))
    print(next(evenIter))
    print(next(evenIter))
    print(next(evenIter))
    print(next(evenIter))
    print(next(evenIter))
    print(next(evenIter))
    print(next(evenIter))

    print(next(evenIter))
