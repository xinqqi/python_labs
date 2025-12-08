# xinqqi
-----
## Лабораторная работа 1
-----
-----
### Задание 1
``` python
name = input("Имя: ")
age = int(input("Возраст: "))
age = age+1
print("Привет, " + name+"! Через год тебе будет "+str(age)+".")
```
<img width="452" height="113" alt="image" src="https://github.com/user-attachments/assets/4e8fd0e8-9a8b-4166-9e27-6b404b1aa42e" />

### Задание 2
``` python
a=input("a: ")
b=input("b: ")
a=a.replace(",",".")
b=b.replace(",",".")
a=float(a)
b=float(b)
sum=a+b
avg=(a+b)/2.0
print("sum: %.2f; avg: %.2f" %(sum, avg))
```
<img width="423" height="100" alt="image" src="https://github.com/user-attachments/assets/9973d934-f1dc-4a79-8097-eba6a934796a" />

### Задание 3
``` python
price=float(input())
discount=float(input())
vat=float(input())
base=price*(1-discount/100)
vat_amount=base*(vat/100)
total=base+vat_amount
print("База после скидки: %.2f" %(base))
print("НДС:               %.2f" %(vat_amount))
print("Итого к оплате:    %.2f" %(total))
```
<img width="382" height="174" alt="image" src="https://github.com/user-attachments/assets/894f905d-193a-497a-99dc-e60aad19a840" />


### Задание 4
``` python
m=int(input("Минуты: "))
h=m//60
m=m%60
print(f"{h:d}:{m:02d}")
```
<img width="363" height="76" alt="image" src="https://github.com/user-attachments/assets/3e03e864-287f-4266-bedf-53d924f19671" />

### Задание 5
``` python
fio = input("ФИО: ")
words = fio.split()

initials = ""
for w in words:
    i = "".join(w[0]).upper()
    initials = initials+i

fio = " ".join(words)
print("Инициалы: "+initials+".")
print("Длина (символов): ", len(fio))
```
<img width="464" height="215" alt="image" src="https://github.com/user-attachments/assets/aed0a3b1-ca1e-4ae9-ba15-66d8fca67b79" />

### Задание 6
``` python
N = int(input())

y = 0
n = 0
i = 1

for i in range(N):
    line = input().split()
    if line[-1].upper() == "TRUE":
        y += 1
    else:
        n += 1

print(y, n)
```
<img width="414" height="193" alt="image" src="https://github.com/user-attachments/assets/f843c515-4589-4962-a9e9-ec4553123e11" />

-----
-----
-----
## Лабораторная работа 2
-----
-----
### Задание 1
``` python
# минимум и максимум
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:

    if not nums:                         # проверка: если пустой, то ValueError
        raise ValueError("пустой список")

    # переменные для min и max, заносим в них значение nums[0]
    max_num = nums[0]
    min_num = nums[0]

    for num in nums:        # поиск min и max
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    return min_num, max_num


def unique_sorted(nums: list[float | int]) -> list[float | int]:   # сортировка

    unique_nums = []        # создаем новый список
    for num in nums:        # проходимся по списку
        # если num - уникальное значение (нет такого же в списке), то заносим в список
        if num not in unique_nums:
            unique_nums.append(num)

    unique_nums.sort()      # сортировка списка по возрастанию
    return unique_nums


def flatten(mat: list[list | tuple]) -> list:       # объединение списков

    flat_list = []        # создаем новый список
    for str in mat:
        # eсли строка/элемент не является списком/кортежем — TypeError
        if not isinstance(str, (list, tuple)):
            raise TypeError
        for item in str:
            flat_list.append(item)      # соединяем
    return flat_list


if __name__ == '__main__':
    print("min/max: --------------------")
    print(min_max([3, -1, 5, 5, 0]))
    print(min_max([42]))
    print(min_max([-5, -2, -9]))
    print(min_max([-7, -1, -2, 3.4, 23, -2, -9.2]))
    # print(min_max([]))
    print(min_max([1.5, 2, 2.0, -3.1]))

    print("sort: --------------------")
    print(unique_sorted([3, 1, 2, 1, 3]))
    print(unique_sorted([]))
    print(unique_sorted([-1, -1, 0, 2, 2]))
    print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))
    print(unique_sorted([-3.34, 1, 5.5, -2.5, 1, -2, 0]))

    print("flatten: --------------------")
    print(flatten([[1, 2], [3, 4]]))
    print(flatten([[1, 2], (3, 4, 5)]))
    print(flatten([[1], [], [2, 3]]))
    print(flatten([[1], (5, -2), [], [2, 4]]))
    # print(flatten([[1, 2], "ab"]))
```
<img width="658" height="377" alt="image" src="https://github.com/user-attachments/assets/2a6e889e-bdd3-4cfa-9ac8-1d01c16b587e" />


### Задание 2
``` python
def transpose(mat: list[list[float | int]]) -> list[list]:  # транспонирование матрицы

    if not mat:         # пустая матрица - пустой список
        return []

    # проверка: если матрица «рваная» (строки разной длины) — ValueError
    str_len = len(mat[0])
    for str in mat:
        if len(str) != str_len:
            raise ValueError("")

    num_str = len(mat)      # строки
    num_stolb = str_len     # столбцы

    # создаем нулевую матрицу
    trans_mat = [[0] * num_str for _ in range(num_stolb)]

    # меняем строки на столбцы, столбцы на строки
    for i in range(num_str):
        for j in range(num_stolb):
            trans_mat[j][i] = mat[i][j]

    return trans_mat


def row_sums(mat: list[list[float | int]]) -> list[float]:  # сумма строк матриц

    if not mat:         # пустая матрица - пустой список
        return []

    # проверка: если матрица «рваная» (строки разной длины) — ValueError
    str_len = len(mat[0])
    for str in mat:
        if len(str) != str_len:
            raise ValueError("")

    num_str = len(mat)   # строки
    num_stolb = str_len  # столбцы

    str_sum_list = []         # создаем пустой список

    for i in range(num_str):
        sumsum = 0
        # считаем сумму каждой строки матрицы и записываем в новый список
        for j in range(num_stolb):
            sumsum += mat[i][j]

        str_sum_list.append(sumsum)

    return (str_sum_list)


def col_sums(mat: list[list[float | int]]) -> list[float]:  # сумма столбцов матрицы

    if not mat:         # пустая матрица - пустой список
        return []

    # проверка: если матрица «рваная» (строки разной длины) — ValueError
    str_len = len(mat[0])
    for str in mat:
        if len(str) != str_len:
            raise ValueError("")

    num_str = len(mat)   # строки
    num_stolb = str_len  # столбцы

    str_sum_list = []

    for j in range(num_stolb):
        sumsum = 0
        # считаем сумму каждого столбца матрицы и записываем в новый список
        for i in range(num_str):
            sumsum += mat[i][j]

        str_sum_list.append(sumsum)

    return (str_sum_list)


print("transpose: --------------------")
matrix1 = [[1, 2, 3]]
matrix2 = [[1], [2], [3]]
matrix3 = [[1, 2], [3, 4]]
matrix4 = []
matrix5 = [[1, 2], [3]]
matrix6 = [[1, 2, 3, 4], [5, 6, 7, 8]]
print(transpose(matrix1))
print(transpose(matrix2))
print(transpose(matrix3))
print(transpose(matrix4))
# print(transpose(matrix5))
print(transpose(matrix6))

print("str sum: --------------------")
matrix7 = [[1, 2, 3], [4, 5, 6]]
matrix8 = [[-1, 1], [10, -10]]
matrix9 = [[0, 0], [0, 0]]
matrix10 = [[1, 2], [3]]
matrix11 = [[-1, 2], [-3, 4]]
matrix12 = [[1.5, 2.5], [3.5, 4.5]]
print(row_sums(matrix7))
print(row_sums(matrix8))
print(row_sums(matrix9))
# print(row_sums(matrix10))
print(row_sums(matrix11))
print(row_sums(matrix12))

print("stolb sum: --------------------")
print(col_sums(matrix7))
print(col_sums(matrix8))
print(col_sums(matrix9))
# print(col_sums(matrix10))
print(col_sums(matrix11))
print(col_sums(matrix12))
```
<img width="718" height="399" alt="image" src="https://github.com/user-attachments/assets/84a7f41d-8c5b-4f4a-8467-e27dbae16718" />


### Задание 3
``` python
def format_record(rec: tuple[str, str, float]) -> str:
    fio, group, gpa = rec

    # проверка на пустое ФИО, пустую группу, неверный тип GPA
    if not fio:
        raise ValueError("empty fio")
    if not group:
        raise ValueError("empty group")
    if not isinstance(gpa, (int, float)):
        raise TypeError("incorrect GPA")

    # разделяем ФИО (убираем все пробелы)
    fio_parts = " ".join(fio.split()).split()

    # заглавная буква для фамилии
    fio_parts[0] = fio_parts[0].capitalize()

    # инициалы (в верхнем регистре), и для ФИО, и для ФИ
    if len(fio_parts) >= 3:
        initials = f"{fio_parts[1][0].upper()}.{fio_parts[2][0].upper()}."
    elif len(fio_parts) == 2:
        initials = f"{fio_parts[1][0].upper()}."

    # записываем все в format_change (группу и GPA тоже))
    format_change = f"{fio_parts[0]} {initials}, гр. {group}, GPA {gpa:.2f}"

    return format_change


print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("пак               анна", "BIVT-25", 4.349)))
print(format_record(("романов    роман   романович", "IKBO-03", 2.567)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.234)))
```
<img width="472" height="130" alt="image" src="https://github.com/user-attachments/assets/80723e55-4773-4556-9d1f-6f88e74352b2" />

-----
-----
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

-----
-----
-----
## Лабораторная работа 4
-----
-----
### Задание A
```python
from pathlib import Path
import csv
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:

    """
    Открыть файл на чтение в указанной кодировке и вернуть содержимое как одну строку.
    Если файл не найден — FileNotFoundError.
    Если кодировка не подходит — UnicodeDecodeError.
    path: путь к файлу.
    encoding: кодировка файла (по умолчанию "utf-8")
        изменить кодировку: encoding="cp1251"
    """

    p = Path(path)
    # FileNotFoundError и UnicodeDecodeError пусть «всплывают» — это нормально
    return p.read_text(encoding=encoding)

def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:

    """
    Создать/перезаписать CSV с разделителем ','.
    header будет записан первой строкой.
    Проверка на одинаковую длину строк (иначе ValueError).
    """

    p = Path(path)
    rows = list(rows)

    if rows:
        row_length = len(rows[0])
        for row in rows:
            if len(row) != row_length:
                raise ValueError("Все строки должны иметь одинаковую длину.")
    
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)

def ensure_parent_dir(path: str | Path) -> None:
    """Создать родительские директории, если их нет."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)

if __name__ == "__main__":
    
    from io_txt_csv import read_text, write_csv
    write_csv([("word", "count"), ("test", 3)], "data/result.csv")
    try:
        txt = read_text("data\lab04\input.txt")
        print("Файл успешно прочитан")
    except FileNotFoundError:
        print("Файл input.txt не найден")
    except UnicodeDecodeError:
        print("Ошибка кодировки при чтении файла")
```
<img width="750" height="289" alt="image" src="https://github.com/user-attachments/assets/2d9a57c0-154d-422f-b7da-6005e11d8d5f" />
<img width="521" height="134" alt="image" src="https://github.com/user-attachments/assets/69c824f4-0b4c-499b-8705-aaf9d9073b14" />

### Задание B
```python
import argparse
import sys
from pathlib import Path

from io_txt_csv import read_text, write_csv
from lib.text import normalize, tokenize, count_freq, top_n

def create_report(input_path: str, output_path: str, encoding: str = "utf-8") -> None:

    """
    Читает входной файл data/lab04/input.txt
    Нормализует, токенизирует и считает частоты слов, используя функции из ЛР3 (lib/text.py)
    Сохраняет data/report.csv c колонками: word,count (отсортированными: count ↓, слово ↑)
    В консоль печатает:
        - кол-во всех слов
        - кол-во уникальных слов
        - топ-5 слов

    Примеры запуска:
        python src/lab04/text_report.py
        python src/lab04/text_report.py --in data/lab04/input.txt --out data/output.csv
        python src/lab04/text_report.py --in data/lab04/input.txt --encoding cp1251

    Если data/input.txt не существует → print() и sys.exit(1)
    Пустой вход → report.csv будет содержать только заголовок.
    Нестандартная кодировка → укажите, как передать --encoding cp1251.
    """

    try:
        text = read_text(input_path, encoding)
    except FileNotFoundError:
        print(f"Ошибка: файл {input_path} не найден.")
        sys.exit(1)
    except UnicodeDecodeError as e:
        print(f"Ошибка: укажите другую кодировку.")
        sys.exit(1)

    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    freq = count_freq(tokens)
    total_words = len(tokens)
    unique_words = len(set(tokens))
    top5 = top_n(freq, 5)

    sorted_data = sorted(freq.items(), key=lambda item: (-item[1], item[0]))
    header = ("word", "count")

    write_csv(sorted_data, output_path, header)
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    for word, count in top5:
        print(f"{word}: {count}")

def main():
    parser = argparse.ArgumentParser(description="Отчёт о частоте слов из текстового файла.")
    parser.add_argument("--in", dest="input_file", help="Путь к входному текстовому файлу.", default="data/lab04/input.txt")
    parser.add_argument("--out", dest="output_file", help="Путь к выходному CSV файлу.", default="data/lab04/report.csv")
    parser.add_argument("--encoding", default="utf-8", )
    args = parser.parse_args()
    create_report(args.input_file, args.output_file, args.encoding)

if __name__ == "__main__":
    main()
```
<img width="777" height="223" alt="image" src="https://github.com/user-attachments/assets/8b6a8f29-a1c4-4a98-af26-e064b6b61f29" />
<img width="805" height="194" alt="image" src="https://github.com/user-attachments/assets/ace5bb98-f50d-4962-9801-d5ba65bb7617" />
<img width="1113" height="349" alt="image" src="https://github.com/user-attachments/assets/5622c852-ef4f-45de-940c-3648f70ad372" />

-----
-----
-----
## Лабораторная работа 5
-----
-----
### Задание A
``` python
from pathlib import Path
import json
import csv

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
    json_file = Path(json_path)
    csv_file = Path(csv_path)

    if not json_file.exists():
        raise FileNotFoundError(f"JSON-файл не найден: {json_path}")
    
    with json_file.open('r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Ошибка чтения JSON-файла (неверный формат или пустой): {e}")
    
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("Все элементы JSON должны быть словарями.")
    if not data or not isinstance(data, list):
        raise ValueError("JSON-файл пустой.")  
    
    first_keys = list(data[0].keys())
    all_unique_keys = set(first_keys)
    for item in data:
        all_unique_keys.update(item.keys())
    add_keys = sorted([k for k in all_unique_keys if k not in first_keys])
    fieldnames = first_keys + add_keys
    
    with csv_file.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            row = {key: item.get(key, "") for key in fieldnames}
            writer.writerow(row)

json_to_csv(f"data/samples/people.json", f"data/out/people_from_json.csv")


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    csv_file = Path(csv_path)
    json_file = Path(json_path)

    if not csv_file.exists():
        raise FileNotFoundError(f"CSV-файл не найден: {csv_path}")
    
    with csv_file.open('r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise ValueError("CSV-файл пуст или отсутствует заголовок.")
        json_data = list(reader)
    if not json_data:
       raise ValueError("CSV-файл пустой.")

    with json_file.open('w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)
        
csv_to_json(f"data/samples/people.csv", f"data/out/people_from_csv.json")
```
![1](https://github.com/user-attachments/assets/2ab516cf-53aa-49eb-a4b9-18e08c2271bf)
![2](https://github.com/user-attachments/assets/c5a34c78-f71a-406d-ac0d-1abde0e43275)

### Задание B
```python
from openpyxl import Workbook
import csv
from pathlib import Path

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Буду использовать openpyxl.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """
    csv_file = Path(csv_path)
    xlsx_file = Path(xlsx_path)

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    if not csv_file.exists():
            raise FileNotFoundError(f"Исходный CSV-файл не найден: {csv_path}")
    with csv_file.open('r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)

    if not rows:
        raise ValueError("CSV файл пустой")

    for row in rows:
        ws.append(row)

    #data_rows = []
        
    for col_idx, col_title in enumerate(ws.columns, start=1):
        max_length = max(len(str(cell.value)) if cell.value is not None else 0 for cell in col_title)
        adjusted_width = max(max_length, 8)
        col_letter = ws.cell(row=1, column=col_idx).column_letter
        ws.column_dimensions[col_letter].width = adjusted_width
    
    wb.save(xlsx_path)

csv_to_xlsx('data/samples/cities.csv', 'data/out/cities.xlsx')
```
![3](https://github.com/user-attachments/assets/bc4b660e-124e-46c8-a7b5-34fdd31f9b9f)

-----
-----
-----
## Лабораторная работа 6
-----
-----
### Задание 1
``` python
import argparse
import sys
from pathlib import Path

sys.path.append('/Users/User/Downloads/python_labs-main/src/lib')
from text import normalize, tokenize, count_freq, top_n

def stats(path, n):
    with open(path, 'r') as text:
        textST = text.read()
        textST = top_n(count_freq(tokenize(normalize(textST))), n)
        print(textST)
        input()

def cat(path, n):
    with open(path,'r') as text:
        catText = text.read()
        catText_normalize = normalize(catText)
        catText_tokenize = tokenize(catText_normalize)
    for i in range(len(catText_tokenize)):
        print(i+1, catText_tokenize[i])

def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    if args.command == "cat":
        """ Реализация команды cat """
        cat(args.input,args.n)
    elif args.command == "stats":
        """ Реализация команды stats """
        stats(args.input,args.top)

input()
main()
```
<img width="1008" height="318" alt="cli_text" src="https://github.com/user-attachments/assets/362e6df1-a8c6-4118-8e8c-221f9d06c3b2" />

### Задание 2
``` python
import argparse
import sys


sys.path.append('/Users/User/Downloads/python_labs-main/src/lab05')
from json_csv import json_to_csv, csv_to_json
from csv_xlsx import csv_to_xlsx


def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv")
    p1.add_argument("--in", dest="input", required=True)
    p1.add_argument("--out", dest="output", required=True)

    p2 = sub.add_parser("csv2json")
    p2.add_argument("--in", dest="input", required=True)
    p2.add_argument("--out", dest="output", required=True)

    p3 = sub.add_parser("csv2xlsx")
    p3.add_argument("--in", dest="input", required=True)
    p3.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()

    """
        Вызываем код в зависимости от аргументов.
    """

    if args.cmd == "json2csv":
        json_to_csv(args.input, args.output)
        print("Completed")

    if args.cmd == "csv2json":
        csv_to_json(args.input, args.output)
        print("Completed")

    if args.cmd == "csv2xlsx":
        csv_to_xlsx(args.input, args.output)
        print("Completed")

main()
```
![convert](https://github.com/user-attachments/assets/ccd8089a-5dcb-4e27-b739-9b0c484e71f4)

-----
-----
-----
## Лабораторная работа 7
-----
-----
### Задание A
``` python
import pytest

from src.lib.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    "text, expected",
    [
        ("ПрИвЕт МИр", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello World", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
    ],
)
def test_normalize(text, expected):
    assert normalize(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("привет, мир!", ["привет", "мир"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("", []),
        ("   ", []),   
    ],
)
def test_tokenize(text, expected):
    assert tokenize(text) == expected


@pytest.mark.parametrize(
    "tokens, expected",
    [
        (["привет", "мир", "привет"], {"привет": 2, "мир": 1}),
        ([], {}),
        (["да"], {"да": 1}),
        (["добрый", "день", "добрый", "вечер"], {"добрый": 2, "день": 1, "вечер": 1}),
    ],
)
def test_count_freq(tokens, expected):
    assert count_freq(tokens) == expected


@pytest.mark.parametrize(
    "freq, n, expected",
    [
        ({"привет": 5, "мир": 3, "пока": 7}, 2, [("пока", 7), ("привет", 5)]),
        ({"да": 3, "нет": 3, "наверное": 3}, 3, [("да", 3), ("наверное", 3), ("нет", 3)]),
        ({}, 5, []),
        ({"ок": 1}, 1, [("ок", 1)]),
        ({"да": 1, "нет": 2}, 10, [("нет", 2), ("да", 1)]),
    ],
)
def test_top_n(freq, n, expected):
    assert top_n(freq, n) == expected
```

<img width="1477" height="915" alt="A_7" src="https://github.com/user-attachments/assets/6f258f73-8b02-4484-8f7c-7022f5643115" />

### Задание B
``` python
import pytest
import json
import csv
from pathlib import Path    

from src.lib.json_csv import json_to_csv, csv_to_json


def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())


def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    rows = [
        {"name": "Alice", "age": "22"},
        {"name": "Bob", "age": "25"},
    ]
    with src.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerows(rows)

    csv_to_json(str(src), str(dst))

    data_out = json.loads(dst.read_text(encoding="utf-8"))

    assert len(data_out) == len(rows)
   # assert all("name" in rec and "age" in rec for rec in data_out)
    assert {"name", "age"} <= set(rows[0].keys())


    def test_json_to_csv_wrong_path():
        with pytest.raises(FileNotFoundError):
            json_to_csv("ошибка: файл json не найден.", "test.csv")

    def test_csv_to_json_wrong_path():
        with pytest.raises(FileNotFoundError):
            csv_to_json("ошибка: файл csv не найден.", "test.json")
```

<img width="1505" height="519" alt="B_7" src="https://github.com/user-attachments/assets/c4024ced-1eaf-4e24-89b1-21c5e0bfcd94" />
