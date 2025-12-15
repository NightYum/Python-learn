class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __getattribute__(self, item):
        if item in ['x', 'y', 'z']:
            return object.__getattribute__(self, item)
        raise AttributeError

    def __setattr__(self, key, value):
        if key in ['x', 'y', 'z']:
            return object.__setattr__(self, key, value)
        raise AttributeError

    def __getattr__(self, item):
        # Вызывается, когда идет обращение к несуществующему аттрибуту класса
        return False

    def __delattr__(self, item):
        object.__delattr__(self, item)

pt1 = Point(1, 2, 3)
pt2 = Point(4, 5, 6)