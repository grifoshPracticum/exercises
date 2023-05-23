ONE = [1, 2, 3]
TWO = [10, 20, 30]


def sum_two_lists(list1, list2):
    return [x + y for x, y in zip(list1, list2)]


print(sum_two_lists(ONE, TWO))
# [11, 22, 33]


def multiply_two_lists(list1, list2):
    return [x + y for x in list1 for y in list2]


print(multiply_two_lists(ONE, TWO))
# [11, 21, 31, 12, 22, 32, 13, 23, 33]
