class Counter:
    def __init__(self):
        self.__count = 0

    def __call__(self):
        self.__count += 1
        print("Counter is called")

c = Counter()
c()

class StripChars:
    def __init__(self, chars):
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError("args must be a string")

        return args[0].strip(self.__chars)

s1 = StripChars("?!:.; ")
result = s1("hello world!!")
print(result)
