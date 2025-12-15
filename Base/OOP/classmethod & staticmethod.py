# @classmethod - метод класса
# @staticmethod - метод, который не имеет доступа к атрибутам и методам класса

class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def set_validate(cls, min_coord, max_coord):
        cls.MIN_COORD = min_coord
        cls.MAX_COORD = max_coord

    @classmethod
    def validate_boolean(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    @classmethod
    def validate(cls, arg):
        if cls.MIN_COORD <= arg <= cls.MAX_COORD:
            return arg
        raise TypeError(f"{cls.MIN_COORD} <= {arg} <= {cls.MAX_COORD} is invalid")

    @staticmethod
    def norm2(x, y, z):
        return x*x + y*y + z*z

    def __init__(self, x, y, z):
        self.x = self.validate(x)
        self.y = self.validate(y)
        self.z = self.validate(z)

    def get_coord(self):
        return self.x, self.y, self.z

vector = Vector(1, 2, 3)
res = vector.get_coord()
norm_x = vector.norm2(1, 2, 3)
print(res, norm_x)