class ThreadData:
    __shared_attrs = {
        "name": "thread1",
        "data": {},
        "id": 1
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs

    def get_attrs(self):
        return self.__dict__

th1 = ThreadData()
th2 = ThreadData()

th2.id = 2
print(th1.get_attrs())
print(th2.get_attrs())