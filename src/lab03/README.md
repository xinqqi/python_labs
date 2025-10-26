# xinqqi
-----
## Лабораторная работа 3
-----
-----
### Задание A
``` python
import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()

    if yo2e:
        text = text.replace('ё', 'е')
        text = text.replace('Ё', 'Е')

    text = re.sub(r'\t\r\n', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()

    return text


def tokenize(text: str) -> list[str]:

    return re.findall(r'\w+(?:-\w+)*', text)


def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for token in tokens:
        if token in freq:
            freq[token] += 1
        else:
            freq[token] = 1

    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_freq = sorted(freq.items(), key=lambda item: (-item[1], item[0]))

    return sorted_freq[:n]


# проверка
assert normalize("дОбРЫй\tДеНь\nчёрныЙ\t") == "добрый день черный"
assert normalize("берёза, КЛён, акТЁР, ещё") == "береза, клен, актер, еще"

assert tokenize("добрый день!!") == ["добрый", "день"]
assert tokenize(
    "хочу себе кресло-качалку.") == ["хочу", "себе", "кресло-качалку"]
assert tokenize("365 дней@") == ["365", "дней"]

freq = count_freq(["a", "b", "a", "b", "c", "a", "b", "a"])
assert freq == {"a": 4, "b": 3, "c": 1}
assert top_n(freq, 2) == [("a", 4), ("b", 3)]

freq2 = count_freq(["bb", "ab", "cc", "ab", "cc"])
assert top_n(freq2, 2) == [("ab", 2), ("cc", 2)]
```
<img width="875" height="588" alt="image" src="https://github.com/user-attachments/assets/4a85974b-69da-4b1b-8066-39a7bfc34aab" />

### Задание B
запуск python -m src.lab03.text_stats ,
конец ввода Ctrl Z + Enter
``` python
import sys
from lib.text import normalize, tokenize, count_freq, top_n

def main():
    text = sys.stdin.read()

    text = normalize(text=text)
    tokens = tokenize(text=text)
    freq = count_freq(tokens)
    top_5 = top_n(freq, 5)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(set(tokens))}")
    print("Топ-5:")
    for word, count in top_5:
        print(f"{word}:{count}")

if __name__ == "__main__":
    main()

# python -m src.lab03.text_stats
```
<img width="313" height="116" alt="image" src="https://github.com/user-attachments/assets/8c75bc2b-2878-405f-b5fe-f1c37eb76662" />
