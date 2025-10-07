def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:

    if not nums:
        raise ValueError("пустой список")
    
    max_num=nums[0]
    min_num=nums[0]

    for num in nums:
        if num>max_num:
            max_num=num
        if num<min_num:
            min_num=num

    return min_num, max_num

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    unique_nums = []
    for num in nums:
        if num not in unique_nums:
            unique_nums.append(num)

    unique_nums.sort()
    return unique_nums

def flatten(mat: list[list | tuple]) -> list:
    flat_list = []
    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError
        for item in row:
            flat_list.append(item)
    return flat_list

if __name__ == '__main__':
    print("min/max: --------------------")
    print(min_max([3, -1, 5, 5, 0]))
    print(min_max([42]))
    print(min_max([-5, -2, -9]))
    print(min_max([-7, -1, -2, 3.4, 23, -2, -9.2]))
    #print(min_max([]))
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
    print(flatten([[1], (5,-2), [], [2, 4]]))
    #print(flatten([[1, 2], "ab"]))