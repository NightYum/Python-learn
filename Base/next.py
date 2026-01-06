nums = [10, 20, 30]

iter_nums = iter(nums)

print(next(iter_nums))
print(next(iter_nums))
print(next(iter_nums))
print(next(iter_nums,  "StopIteration"))

messages = ["Шифр не найден", "Точка сбора на улице Ленина", "Уточнение к миссии 7А"]

print(
    next(
        (w for msg in messages for w in msg.split() if any(map(str.isdigit, w))),
        'Кодовое слово не найдено'
    )
)
