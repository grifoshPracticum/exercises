# Создать функцию которая принимает 2 массива и выдает массив первый элемент которого равен сумме
# первого элемента первого массива и последнего элемента второго массива
# второй - сумма второго элемента первого массива и предпоследнего элемента второго массива

# Функция принимает массив массивов [[1,2,3], [11,22,33], [111,222,333,444], [5,5,3,2], [3]].
# Надо:
#      а. Выдать сумму всех чисел
#      б. Выдать все в одном массиве: [1,2,3,1,2,3,1,2,3,4,5,5,3,2,3]
#      в. Выдать массив, массивов, где первый - это все элементы под индексом 0,
#         второй - все элементы под индексом 1, и так далее.
#         Например: [[1,11,111,5,3],[2,22,222,5,None],...]


def summ_of_all_elements(list_of_lists):
    summ_of_all_elements = 0
    for one_list in list_of_lists:
        summ_of_all_elements += sum(one_list)
    return summ_of_all_elements

print(summ_of_all_elements([[1, 2, 3], [10, 20, 30]]))