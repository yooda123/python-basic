class Duck:
    """
    This is a class for Duck.

    Attributes:
      name (str): the name of the duck

    Methods:
      wask: print ***
      quack: print ***
      fly: print ***
    """

    def __init__(self, name) -> None:
        """
        The Constructor for Duck class
        :param name:
        """
        self.name = name

    def walk(self):
        print("walking...")

    def quack(self):
        print("quack quack...!")

    def fly(self):
        print("Whee!!")


class Penguin:
    def __init__(self, name) -> None:
        self.name = name

    def walk(self):
        print("walking,,,")

    def quack(self):
        print("quack quack...??")

    def swim(self):
        print("Swmming!!")


def walk_and_quack(duck):
    print(f"I'm {duck.name}.")
    duck.walk()
    duck.quack()


if __name__ == '__main__':

    donald = Duck("Donald")
    pingu = Penguin("pingu")

    # donald.walk()
    # donald.quack()
    # pingu.walk()
    # pingu.quack()
    # walk_and_quack(donald)
    # walk_and_quack(pingu)

    duck_list = [donald, pingu]
    for duck in duck_list:
        walk_and_quack(duck)
