from random import randint


class House:
    def __init__(self):
        self.food = 50
        self.money = 0


class Homelander:
    def __init__(self, name: str, house):
        self.name = name
        self.satiety = 50
        self.house = house

    def live_day(self):
        if self.satiety < 20 and self.house.food >= 15:
            return self.eat()
        elif self.house.food < 15:
            return self.shopping()
        elif self.house.money < 50:
            return self.work()

        rand = randint(1, 6)

        if rand == 1:
            return self.work()
        elif rand == 2:
            return self.eat()
        else:
            return self.play()

    def is_alive(self):
        if self.satiety <= 0:
            return False
        return True

    def work(self):
        self.house.money += 10
        self.satiety -= 20

    def eat(self):
        self.satiety += 15
        self.house.food -= 15

    def play(self):
        self.satiety -= 20

    def shopping(self):
        self.house.money -= 30
        self.house.food += 20


house1 = House()
house2 = House()
h1 = Homelander('Андрюша', house1)
h2 = Homelander('Владюша', house2)

for i in range(100):
    if h1.is_alive():
        h1.live_day()
        if (i + 1) % 5 == 0:
            print(f'День {i + 1}. Статы: Сытость - {h1.satiety}, '
                f'Еда в доме - {h1.house.food}, Деньги в доме - {h1.house.money}')
    else:
        print(f'{h1.name} скончался. Он прожил {i + 1} дней')
        break
