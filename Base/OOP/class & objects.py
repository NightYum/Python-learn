"""OOP"""
# __name__ = "My code"
#
# print(__doc__, __name__)

class Point:
    color = "red"
    circle = 2

# Операции с атрибутами/свойствами класса
Point.color = "black"

print("Получение атрибута класса:", Point.circle)

print("Получение всех атрибутов класса:", Point.__dict__)

# Экземпляры класса, которые образуют своё пространство имен
a = Point()
b = Point()

#
print("Получение типа объекта:", type(a))
print("Проверка класса через объект:", type(a) == Point)
print("Проверка только через isinstance()", isinstance(a, Point))

print("Проверка, принадлежит ли экземпляр класса к тому же что и b: ",type(a) == type(b))

# Док-во того, что экземпляр класса не содержит своих атрибутов, до тех пор пока мы не присвоим к экземпляру класса новый атрибут
print(a.__dict__, b.__dict__)
print(a.color, b.color)

a.color = "red"
print(a.__dict__, b.__dict__)

# Способы добавить новые атрибуты в класс
Point.radius = 10
setattr(Point, "s", 15)

# Способы получить атрибуты из класса, третьим аргументом пишется то, что мы получим, если данного атрибута не будет в классе
print(Point.radius)
print(getattr(Point, "s"))
print(getattr(Point, "none", [False, None]))

# Способы проверить есть ли атрибут в классе
try:
    print(Point.none)
except AttributeError:
    print("AttributeError")

print(hasattr(Point, "color"))

# Способы удаление атрибута класса
del Point.radius
delattr(Point, "s")

# Как правильно удалить атрибут, чтобы не было ошибки

def delattr_from_class(object: object, attr: str):
    if hasattr(object, attr):
        delattr(object, attr)
        print("delattr_from_class Attribute has been deleted")
    else:
        print("delattr_from_class AttributeError")

delattr_from_class(Point,'s')

# Если удалить атрибут у экземпляра класса, то он вернется
a.color = "red"
delattr_from_class(a,'color')
print(a.color)