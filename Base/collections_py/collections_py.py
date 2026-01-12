from collections import Counter, defaultdict

count_char = Counter("Haha, merry")
dict_count_char = dict(count_char)

print(count_char)
print(dict_count_char)

count_num = Counter([1, 2 ,2, 3, 4, 5, 1 ,2])
dict_count_num = dict(count_num)

print(count_num)
print(count_num.most_common())
print(dict_count_num)


text = "cat dog cat bird dog cat"
count_text = Counter(text.split())

print(count_text)

count_num1 = Counter([1, 1, 2, 3, 3, 3])
generator = [x for x, n in count_num1.items() if n > 1]
print(generator)


df = defaultdict(int)
for x in [1, 2, 2, 3]:
    df[x] += 1

print(df)
string = "12"
for i, j in string, range(len(string)):
    print(i, j)

d = {(1, 2, 3): "Hello world",
     (1, 2, 4): "Hello ",
     }

print(d[1, 2, 4])