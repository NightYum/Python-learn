# __new__ - вызывается перед созданием объекта класса


class Point:
    def __new__(cls, *args, **kwargs):
        print(f"__new__ self= {cls}")
        return super().__new__(cls)

    def __init__(self, x=0, y=0):
        print(f"__init__ self= {self}")
        self.x = x
        self.y = y

pt = Point(10, 20)
print(pt)

# __new__ self= <class '__main__.Point'>
# Все классы наследуются от базового класса object
# При помощи super() мы получаем ссылку на базовый класс

# Пример поведения Singleton
class Database:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if Database.__instance is None:
            cls.__instance =  super().__new__(Database)
            return cls.__instance
        return cls.__instance


    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"Connecting to database: {self.user} {self.psw} {self.port}")


db = Database("user", "psw", "port")
print(db)
db2 = Database("user", "psw", "port")
print(db2)