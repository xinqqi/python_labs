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
