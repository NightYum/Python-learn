# str - для отображения информации об объекте для класса пользователей
# repr - для отображения информации об объекте класса в режиме отладки
# len - позволяет применять функцию len() к экземплярам класса
# abs - позволяет применять функции abs() к экземлярам класса
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __len__(self):
        return len(self.__dict__)

    def __abs__(self):
        return list(map(abs, [self.x, self.y]))

pt1 = Point(1,-2)
print(pt1)
print(str(pt1))
print(len(pt1))
print(abs(pt1))
print(repr(pt1))