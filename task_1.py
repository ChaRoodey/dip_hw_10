class Parent:
    def __init__(self, name: str, age: int, childs_id: list) -> None:
        self.name = name
        self.age = age
        self.childs_id = childs_id

    def call(self):
        print(f'Привет! Меня зовут {self.name}, мне {self.age} лет '
              f'и у меня есть дети: {(i for i in self.childs_id)}')

    def calm(self, child_id: int):
        if child_id in self.childs_id:
            if not child_id.calm_stat:
                child_id.calm_stat = True
                print('Ребенок теперь успокоен')
            else:
                print('Ребенок и так был спокоен')

        else:
            print('Это не мой ребенок!')

    def feed(self, child_id: int):
        if child_id in self.childs_id:
            if not child_id.feed_stat:
                child_id.feed_stat = True
                print('Ребенок теперь сыт')
            else:
                print('Ребенок и так был сыт')
        else:
            print('Это не мой ребенок!')


class Child:
    def __init__(self,child_id: int, name: str, age: int, calm_stat, feed_stat: bool) -> None:
        self.child_id = child_id
        self.name = name
        self.age = age
        self. calm_stat = calm_stat
        self.feed_stat = feed_stat


if __name__ == '__main__':
    p1 = Parent('Виталя', 37, [1, 3])
    p2 = Parent('Марина', 22, [2])
    ch1 = Child(1, 'Олежка', 5, True, False)
    ch2 = Child(2, 'София', 10, False, True)
    ch3 = Child(3, 'Инокентий', 15, False, True)

    p1.call()
    p2.call()
    p1.calm(1)
