from collections import Counter, defaultdict

WORDS = "one two two three three three four four four four"

def count_words(sentence: str | list[str]) -> None:
    words = sentence.split() if isinstance(sentence, str) else sentence

    counts = Counter(words)
    df: defaultdict[str, list] = defaultdict(list)

    for word, freq in counts.items():
        df[freq].append(word)

    print(df)



def main():
    count_words(WORDS)

if __name__ == "__main__":
    main()