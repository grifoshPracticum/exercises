# ------------------------------------------------------- String task:
# Является ли строка неизменяемым типом данных в python?
# s = 'Hello, World!'
# print(id(s))
# a = (s.replace("o", "i"))                        # "Helli, Wurld!"
# print(id(a))
#
# Ответ: не является, replace - это другое :)


# ------------------------------------------------------- Lists tasks:
# 1. Сделать функцию, которая принимает массив чисел, возводит в квадрат каждое и суммирует.                         #OK
# Input:    [2,5,7]
# Output:   78

# def sumMultiply(my_list):
#     return sum(x**2 for x in my_list)
#
# a = [2, 5, 7]
# print(sumMultiply(a))


# my_list = [2, 5, 7]
# result = 0
# for x in my_list:
#     result += x**2
# print(result)


# my_list = [2, 5, 7]
# result = sum(x**2 for x in my_list)
# print(result)


# my_list = [2, 5, 7]
# result = sum([x**2 for x in my_list])
# print(result)



# 2.1 Сделать функцию, которая принимает 2 массива и складывает их поэлементно                                       #OK
# Input: [1,2,3], [10,20,30]
# Output: 11, 22, 33.

# def combine_lists_by_element(list1, list2):
#     new_list = []
#     if len(list1) != len(list2):
#         arise('Count of entries in lists is not matched')
#     for i, element in enumerate(list1):                                                    # return enumerate object
#         new_element = element + list2[i]                                                   # как бы тут без list1[i]?
#         new_list.append(new_element)
#     return new_list
# combine_lists_by_element([1,2,3], [10,20,30])


# def combine_lists_by_element2(list1, list2):
#     new_list = []
#     if len(list1) != len(list2):
#         arise('Count of entries in lists is not matched')
#     for element1, element2 in zip(list1, list2):
#         new_list.append(element1+element2)
#     return new_list

# combine_lists_by_element2([1,2,3], [10,20,30])


#попробуй list comprehesion                                                                                   #to_review
# def combine_lists_by_element(list1, list2):
#     if len(list1) != len(list2):
#         raise ValueError('Count of entries in lists does not match')
#     return [element1 + element2 for element1, element2 in zip(list1, list2)]
#
# list1 = [1, 2, 3]
# list2 = [10, 20, 30]
# result = combine_lists_by_element(list1, list2)
# print(result)




# def combine_lists_by_element2(list1, list2):
#     new_list = []
#     if len(list1) != len(list2):
#         arise('Count of entries in lists is not matched')
#     for element1, element2 in zip(list1, list2):
#         new_list.append(element1+element2)
#     return new_list

# combine_lists_by_element2([1,2,3], [10,20,30])


# new_list = [expression for item in iterable if condition]
# def combine_lists_by_element(list1, list2):
#     if len(list1) != len(list2):
#         raise ValueError('Error: count of entries in lists does not match')
#
#     new_list = [list1[i] + list2[i] for i, element in enumerate(list1)]
#     return new_list
#
#
# combine_lists_by_element([1, 2, 3], [10, 20, 30])


# Сделать функцию, которая принимает два массива, складывает первый и последний элемент
# записывает в новый массив на первое место, второй и предпоследний на второе и так далее.
# Например func([1,2,3], [10,20,30])=> [31, 22, 13]

# def combine_lists(list1, list2):
#     new_list = []
#     if len(list1) != len(list2):
#         arise('Count of entries in lists is not matched')
#     for i in range(len(list1)):                                                                   #не по-питоновски ;)
#         new_element = list1[i] + list2[-i-1]
#         new_list.append(new_element)
#     return new_list

# combine_lists([1,2,3], [10,20,30])


# python enumirate
# Как итерироваться по 2 массивам?
# Говорили, что .append - медленный способ

def combine_lists(list1, list2):                                                                                  #to_do
    # Чем .extend отличается от .append?
    if len(list1) != len(list2):
        raise ValueError('Count of entries in lists is not matched')
    new_list = []
    # Как создать пустой massive с длиной list1?
    for i in range(len(list1)):
        new_element = list1[i] + list2[-i-1]
        new_list.extend([new_element])                                                           # lvl непросвещенный :)
                                                                                                 # А давай-ка с list comprehension :)
    return new_list

print(combine_lists([1, 2, 3], [10, 20, 30]))




# 4. Функция принимает массив массивов [[1,2,3], [11,22,33], [111,222,333,444], [5,5,3,2], [3]]. Надо
#    a. Выдать сумму всех чисел
#    б. Выдать все в одном массиве: [1,2,3,1,2,3,1,2,3,4,5,5,3,2,3]
#    в. Выдать массив, массивов, где первый - это все элементы под индексом 0, второй - все элементы под индексом 1, и так далее. Например: [[1,11,111,5,3],[2,22,222,5,None],...]






# # tuples tasks:
# 1. Write a Python program to add an item to a tuple in a specific index
def add_item_to_tuple(tuple_obj, item, index):
    if index < 0 or index > len(tuple_obj):                                       # Этот код не добавляет ничего нового
        raise IndexError('Index out of range')                                    # к стандартному обработчику python
    new_tuple = tuple_obj[:index] + (item,) + tuple_obj[index:]
    return new_tuple

# 2. Напиши функцию которая принимает тупл и делает его клон
#    (надо тут еще обсудить такое понятие как scope)

# 3.1
#   Напиши функцию которая превращает кортеж в число:
#   Input (1,2,7)
#   Output: 127






# 3.2
#   И еще одну которая делает обратно:
#   Input: 127
#   Output:(1,2,7)

# def int_to_tuple(my_int):
#     str_int = str(my_int)
#     digits = []
#     for digit in str_int:
#         digits.append(int(digit))
#     return tuple(digits)
# print(int_to_tuple(127))
#
# def int_to_tuple2(my_int):
#     str_int = str(my_int)
#     digits = [int(digit) for digit in str_int]
#     return tuple(digits)
# print(int_to_tuple2(127))
#
# def int_to_tuple(number):
#     digits = [int(digit) for digit in str(number)]
#     return tuple(digits)
# print(int_to_tuple(127))

