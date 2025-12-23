# Метода арифметических операций
# add - для операции сложения
# sub - для операции вычитания
# mul - для операции умножения
# truediv - для операции деления

class Clock:
    __DAY = 86400

    @classmethod
    def check_value(cls, value):
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")
        return value

    def __init__(self, seconds: int):
        self.check_value(seconds)
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        n = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24

