# __ имя магического метода __
# __init__ - вызывается сразу после создания объекта класса

class Point:
    color = "red"
    circle = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __del__(self):
        # Происходит автоматически, когда работает сборщик мусора Python
        print("Удаление экземпляра", str(self))

    def set_coords(self, x, y):
        self.x = x
        self.y = y
        print("Вызов метода set_coords()", str(self))

    def get_coords(self):
        return (self.x, self.y)

pt = Point(10, 20)
print(pt.__dict__)