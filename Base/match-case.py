string = "Python"
string2 = "Py"

match string2:
    case "Python" | "Py":
        print("P")
    case "Golang":
        print("G")
    case _:
        print("No")

number = 8
match number % 2:
    case 0:
        print("Чётное число")
    case 1:
        print("Нечётное число")

# Меняйте значение переменной value для тестирования
value = [1, 2, 3]

match value:
    case int() | float():  # Проверяем, является ли число целым или с плавающей точкой
        print("Имеем дело с числом")
    case str():  # Проверяем, является ли строкой
        print("Имеем дело со строкой")
    case list():  # Проверяем, является ли списком
        print("Имеем дело со списком")
    case _:  # Если ни один из типов не подошёл
        print("Лучше с этим дел не иметь")
