import random


# free_list - список(пул) уже освобожденных объектов,
# которые питон не возвращает системе,
# а оставляет для повторго использования

def tuples_caching():
    size = random.randint(1, 100)
    t = tuple(random.sample(range(1000), size))
    print(id(t), size)

for i in range(5):
    tuples_caching()