numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers[3] = 5
print(numbers[3])

numbers.append(11)
print(numbers)

numbers.insert(5, 10)
print(numbers[5])

numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numbers + numbers2)

numbers.append('hello')
print(numbers)

print(numbers.pop(2))
print(numbers)

numbers.remove(10)
print(numbers)

numbers2.clear()
print(numbers2)

numbers.extend([10, 20, 30])
print(numbers)

print(numbers[5:])
print(numbers[:5])
print(numbers[2:5])
print(numbers[1:7:2])
print(numbers[::2])

numbers3 = numbers[2:6]
numbers4 = numbers3[:]
print(numbers3)
print(id(numbers3), id(numbers4))

big_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_big_numbers = big_numbers[:]
print(new_big_numbers)
del new_big_numbers[::2]
print(new_big_numbers)
new_big_numbers[2:6:2] = [100, 200]
print(new_big_numbers)

# В extend передается только итерируемый объект
list_names = ["Michael", "Bob", "Jim"]
list_names.extend("abc")
print(list_names)
# # Должна быть ошибка TypeError
# list_names.extend(True)
# print(list_names)

print("<>".join("list_names"))