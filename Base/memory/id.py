import copy

a = 100
b = a

print(f"a = 100 b = a")
print(f"id(a): {id(a)}")
print(f"id(b): {id(b)}")
print(f"id(a) == id(b)? {id(a) is id(b)}")

print()

a += 1
print(f"a += 1")
print(f"id(a): {id(a)}")
print(f"id(b): {id(b)}")
print(f"id(a) == id(b)? {id(a) is id(b)}")

print()

print("copy")
list_a = [1, 2, 3]
list_a_copy = copy.copy(list_a)
print(f"list_a = {list_a} id = {id(list_a)}")
print(f"list_a_copy = {list_a_copy} id = {id(list_a_copy)}")
print(f"list_a[0] == list_a_copy[0]? {list_a[0] is list_a_copy[0]}")

print()
# == - проверяет значение
# is - проверяет указывает ли два объекта на один тот же объект в памяти
# Что то deepcopy не работает, возможно Python оптимизирует эту часть
print("deepcopy")
list_b = [1, 2, 3]
list_b_copy = copy.deepcopy(list_b)
print(id(list_b[0]), id(list_b_copy[0]))
print(f"list_b = {list_b} id = {id(list_b)}")
print(f"list_b_copy = {list_b_copy} id = {id(list_b_copy)}")
print(f"list_b[0] ==  list_b_copy[0]? {list_b[0] is list_b_copy[0]}")

print()

# Пример с листами
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(f"l1 = {l1} id = {id(l1)}")
print(f"l1 is l2 = {l1 is l2}")
print(f"l1 == l2 = {l1 == l2}")

print()

# Пример с только что созданными объектами
# print(() is ()) - не работает, хотя в других реализациях или версиях питона может работать PyPy, Micropython, Jython
print(f"[] is []? {[] is []}")
print(f"tuple() is tuple()? {tuple() is tuple()}")

