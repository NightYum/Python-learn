x, y = 5, 10
print(f"{x = }, {y = }")

# {значение: [fill][align][width]}
# Со строками по умолчанию значение сдвигается к левому краю
# С числами по умолчанию значение сдвигается к правому краю

string = "Hello"

print(f"{string:10}")
print(f"{string:-<10}")
print(f"{string:->10}")
print(f"{string:-^10}")

number = 100
print(f"{number:5}")
print(f"{number:-<5}")
print(f"{number:->5}")
print(f"{number:-^5}")

float_number = 7.2365
print(f"{float_number:.5f}")
print(f"{float_number:.2f}")
print(f"{float_number:-^10.2f}")

big_number = 1000000
print(f"{big_number:,d}")
print(f"{big_number:_d}")

print()

items = ['banana', 'apple', 'orange']
price = [10, 20, 30]
amount = [1, 2, 3]

print(f"{'SHOP':=^49}")
print(f"#{'item':^15}|{'price':^15}|{'amount':^15}#")
for i in range(0, 3):
    print(f"#{items[i]:^15}|{price[i]:^15}|{amount[i]:^15}#")
print("="*49)

# ======================SHOP=======================
# #     item      |     price     |    amount     #
# #    banana     |      10       |       1       #
# #     apple     |      20       |       2       #
# #    orange     |      30       |       3       #
# =================================================