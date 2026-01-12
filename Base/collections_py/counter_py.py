from collections import Counter

string = "abrakadabra"
res = Counter(string)
print(res)

info_list = ["abc", "bca", "ABC", "bca"]
res = Counter(info_list)
print(res)

info_tuple = (1, 2, 3, 4, 5, 5, 0, 9, 8, 7)
res = Counter(info_tuple)
print(res)

# Можно передавать словари таким образом
# Наследуется от словаря dict
obj_counter_one = Counter({"x": 1, "y": 0})
obj_counter_two = Counter(x=1, y=0)

print(obj_counter_one, obj_counter_two)

# Возвращает 0, если ключа нет
print(obj_counter_one["none_obj"])

# update в Counter
obj_counter_names = Counter({"Mikhail": 1, "Bot": 2})
obj_counter_names.update({"Noob": 1, "Bot": 1})

print(obj_counter_names)
# Вернуться все ключи
print(obj_counter_names.most_common())
# Вернется только два ключа
print(obj_counter_names.most_common(2))

# Возвращает итератор
iter_counter_names = obj_counter_names.elements()
print(list(iter_counter_names))
print(tuple(iter_counter_names))
print(set(iter_counter_names))

# Вернет сумму значений всех элементов
print(obj_counter_names.total())

c1 = Counter(a=1, b=2, c=3)
c2 = Counter(b=2, d=3, f=2)
print(c1 + c2)
# При вычитании ключи с отрицательными значениями будут удалены
print(c1 - c2)
# Выведет
print(c1 | c2)
# Выведет общие ключи
print(c1 & c2)
# Если нужно вычислить и отрицательные значения без их удаления
c1.subtract(c2)
print(c1)