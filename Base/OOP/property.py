# property

class User:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def get_old(self):
        return self.__old

    @get_old.setter
    def old(self, new):
        self.__old = new

    @old.deleter
    def old(self):
        del self.__old

    # old = property()
    # old = old.setter(set_old)
    # old = old.getter(get_old)

user1 = User("John", 123)
print(user1.get_old)