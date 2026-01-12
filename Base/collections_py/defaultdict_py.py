from random import randint
from collections import defaultdict
from collections.abc import Iterable

SOME_SENTENCE = (
    "car", "name", "car", "house", "name"
)

SOME_NAMES = ["Mikhail", "Bob", "Jake", "Aic", "Kinoki", "Fred", "Mikhail"]

SOME_PLACES_WITH_PEOPLE = {
"The Red Square": {"Ivan", "Olga", "Peter", "Sergey"},
"Thé Big Ben": {"Kate", "Ivan", "Charles", "Olga"},
"The Golden Bridge" : {"John", "Ivan", "Kate", "Peter"},
}

def my_func():
    return bool(randint(0, 1))

def counter(start=1):
    def wraps_counter():
        nonlocal start
        start += 1
        return start

    return wraps_counter()

def test_bool_func():
    df: defaultdict[int, bool] = defaultdict(my_func)

    for i in range(0, 100):
        df[i]

    print(df)

def test_counter_func() -> None:
    # Можно написать свою функцию, и присваивать ссылку,
    # а уже после, когда понадобится вызывать её
    df: defaultdict[int, int] = defaultdict(counter)

    for i in range(0, 100):
        df[i]

    print(df)


def count_words_in_sentence_wo_df(sentence: tuple) -> None:
    words_count: dict[str, int] = {}
    for word in sentence:
        if word not in words_count:
            words_count[word] = 0
        words_count[word] += 1

    print(words_count)

def count_words_in_sentence_with_df(sentence: tuple) -> None:
    words_count: defaultdict[str, int] = defaultdict(int)
    for word in sentence:
        words_count[word] += 1

    print(words_count)

def df_w_lambda():
    df: defaultdict[str, int] = defaultdict(lambda: randint(0, 100))

    # PyCharm заставляет ставить переменную из-за аннотаций типов
    # Хотя явно было бы лучше не перезаписывать это в переменную для лучшей производительности
    for i in range(0, 100):
        df[str(i)]
        # _ = df[str(i)]  Прости вот так

    # Метод с генератором не так эффективен, потому что мы лишний раз создаем список
    # который после заполняем
    # _ = [df[str(i)] for i in range(0, 100)]

    print(df)

def group_names_by_length(list_names: Iterable[str]) -> None:
    names_by_length: defaultdict[str, set[str]] = defaultdict(set)

    for name in list_names:
        names_by_length[len(name)].add(name)

    for count, names in sorted(names_by_length.items(), reverse=True):
        print("===", count)
        print(names)

    print(names_by_length)

def may_seen_each_other(places_with_people) -> None:
    # Можно type не писать, будет работать и так
    type Places_withPeople = defaultdict[str, defaultdict[str, set]]
    places_where_seen_each_other: Places_withPeople = defaultdict(
        lambda: defaultdict(set)
    )
    # Тут можно заменить на Itertools Combinations
    for venue, people in places_with_people.items():
        for person1 in people:
            for person2 in people:
                if person1 != person2:
                    places_where_seen_each_other[person1][venue].add(person2)

    seen = (
        "Olga" in places_where_seen_each_other["Ivan"]["The Red Square"]
        #  Лучше не вызывать thunder методы
        #  places_where_seen_each_other["Ivan"]["Places_withPeople"].__contains__("Olga")
    )
    print("Ivan seen Olga at The Red Square:", seen)
    print()



def main():
    test_bool_func()
    test_counter_func()
    count_words_in_sentence_wo_df(SOME_SENTENCE)
    count_words_in_sentence_with_df(SOME_SENTENCE)
    df_w_lambda()
    group_names_by_length(SOME_NAMES)
    may_seen_each_other(SOME_PLACES_WITH_PEOPLE)

if __name__ == "__main__":
    main()