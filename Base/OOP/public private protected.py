# public - публичное свойство
# protected _name_ - служит для обращения внутри класса и во всех его дочерних классах
# private __name__ - служит для обращения только внутри класса


class Point:
    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x, y, z):
        self.x = x
        self._y = y
        self.__z = z

    def __check_values(cls, *args):
        if not all(isinstance(arg, (int, float)) for arg in args):
            raise TypeError("Argument must be an int")
        if not all(cls.MIN_COORD <= arg <= cls.MAX_COORD for arg in args):
            raise ValueError("Argument must be between 0 and 100")
        return True
    # setter - интерфейсы для работы с атрибутами
    def set_coord(self, *args):
        self.__check_values(*args)
        self.x = args[0]
        self._y = args[1]
        self.__z = args[2]


    def set_access(self, arg: str, protect: int):
        self.__check_values(arg)
        access = {
            1: "",
            2: "_",
            3: "__",
        }
        name = access[protect] + arg
        setattr(self, name)

    # getter
    def get_coord(self):
        return self.x, self._y, self.__z

pt = Point(1, 2, 3)
pt.set_coord(1, 0, 2)
print(pt._Point__z)