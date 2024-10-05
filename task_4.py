class Animal:
    def __init__(self, name):
        self.name = name


class Bird(Animal):
    def __init__(self, wingspan: int):
        self.wingspan = wingspan
        super().__init__(Animal)

    def wing_length(self):
        return self.wingspan * 2


class Fish(Animal):
    def __init__(self, max_depht: int):
        self.max_depht = max_depht
        super().__init__(Animal)

    def depth(self):
        if self.max_depht < 10:
            return 'Мелководная рыба'
        elif self.max_depht > 100:
            return 'Глубоковдная рыба'
        else:
            return 'Средневодная рыба'


class Mammal(Animal):
    def __init__(self, weight: int):
        self.weight = weight
        super().__init__(Animal)

    def category(self):
        if self.weight < 1:
            return 'Малявка'
        elif self.weight > 200:
            return 'Гигант'
        else:
            return 'Обычный'


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, *args):
        if animal_type == 'bird':
            b = Bird(*args)
        elif animal_type == 'fish':
            b = Fish(*args)
        elif animal_type == 'mammal':
            b = Mammal(*args)
        else:
            print('Недопустимый тип животного')


if __name__ == '__main__':
    animal = AnimalFactory()
    animal.create_animal('Олежа', 'bird', 5)
