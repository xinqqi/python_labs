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
