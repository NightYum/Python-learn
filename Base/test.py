class Stack:
    def __init__(self):
        self.__stack = []
        self.min_value = None


    def push(self, value: int):
        self.__stack.append(value)
        print("init", self.__stack)

    def pop(self) -> int:
        return self.__stack.pop()

    def top(self) -> int:
        return self.__stack[-1]

    def get_min_value(self) -> int:
        return self.min_value

my_stack = Stack()
my_stack.push(1)
my_stack.push(10)
my_stack.push(15)
b = []

print(my_stack.get_min_value())
# callable()

dict1 = {"Misha": 18, "No": 20}
print(list(dict1), list(dict1.values()))
print(dict1.keys(), dict1.values())
print(dict1.items())