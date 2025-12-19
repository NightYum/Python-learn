# non-data descriptor - дескриптор не данных, он только дает даннные
# data descriptor - дескриптор данных, дает, меняет данные

class Integer:
    def __set_name__(self, owner, name):
        print("__set_name__ called")
        self.name = " " + name

    def __get__(self, instance, owner):
        print("__get__ called")
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print("__set__ called", value)
        instance.__dict__[self.name] = value

    def __del__(self, instance):
        del instance.__dict__[self.name]

class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def verify_coord(cls, coord):
        if isinstance(coord, int):
            raise TypeError('Coordinate must be an integer')

    @property
    def x(self):
        return self.x

    @x.setter
    def x(self, coord):
        self.verify_coord(coord)
        self.x = coord