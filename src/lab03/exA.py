import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()

    if yo2e:
        text = text.replace('ё', 'е')
        text = text.replace('Ё', 'Е')

    text = re.sub(r'[\x00-\x1f\x7f-\x9f]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()

    return text

def tokenize(text: str) -> list[str]:
    i = r'\w+(?:-\w+)*'                 # (?:-\w+)* - незахватываемая группа
    return re.findall(i, text)

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
    # задаем функцию сортировки и сортируем. функция получает item (токен, частота)
    # и возвращает (-частота, токен)

    return sorted_freq[:n]



# проверка

assert normalize("дОбРЫй\tДеНь\nчёрныЙ\t") == "добрый день черный"
assert normalize("берёза, КЛён, акТЁР, ещё") == "береза, клен, актер, еще"

assert tokenize("добрый день!!") == ["добрый", "день"]
assert tokenize("хочу себе кресло-качалку.") == ["хочу", "себе", "кресло-качалку"]
assert tokenize("365 дней@") == ["365", "дней"]

freq = count_freq(["a","b","a","c","b","a"])
assert freq == {"a":3, "b":2, "c":1}
assert top_n(freq, 2) == [("a",3), ("b",2)]

freq2 = count_freq(["bb","aa","bb","aa","cc"])
assert top_n(freq2, 2) == [("aa",2), ("bb",2)]