class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def walk(self):
        print(f"{self.name} is walking!")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking!!")


def walk_with_me(animal: Animal) -> None:
    # if type(animal) is Animal: #subclassは拾わない！！
    #     animal.walk()

    # if isinstance(animal, Animal): #これでも良いが、振る舞いをチェックするのがpython
    #     animal.walk()
    method = getattr(animal, 'walk', None)
    if callable(method):
        animal.walk()
    else:
        raise TypeError(f"{type(animal).__name__}は散歩(walk)できません")


if __name__ == '__main__':
    # pochi = Animal("Pochi")
    # walk_with_me(pochi) # "pochi is walking!"

    pochi = Dog("Pochi")
    walk_with_me(pochi)  # subclassは拾われず、表示されない　"pochi is walking!"
