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