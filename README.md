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
