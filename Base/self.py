class Point:
    color = "red"
    circle = 2

    def set_coords(self, x, y):
        self.x = x
        self.y = y
        print("Вызов метода set_coords()", str(self))

    def get_coords(self):
        return (self.x, self.y)

    def check_self(self, new_self):
        print(self == new_self)

print(Point.set_coords)
Point.set_coords(Point, x=10, y=20)


print()


pt = Point()
pt2 = Point()

# Док-во того что автоматически подставляется self в качестве первого элемента
pt.check_self(new_self=pt)

# Ссылка на экземпляр класса
print(pt.set_coords)

# Добавление в экземпляр класса новых свойств
pt.set_coords(x=2, y=3)
print(pt.__dict__)

pt2.set_coords(x=20, y=30)
print(pt2.__dict__)

print(pt.get_coords())

function_get_coords = getattr(pt, "get_coords")
print(function_get_coords())