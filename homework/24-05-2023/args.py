# тривиальная задача на синтаксис:
# напиши функцию которая принимает произвольное число итераторов содержащих числа и выдает сумму всех чисел

A = [10, 20, 30]            # list
B = (i for i in range(3))   # generator
C = (100, 200, 300)         # tuple

print(B)
print(sum(B))

def sum_of_iterators(*iter_objects):
    total_sum = 0
    for iterator in iter_objects:
        total_sum += sum(iterator)
    return total_sum


def sum_of_iterators2(*iter_objects):
    return sum(
        [sum(iterator) for iterator in iter_objects]
    )


result = sum_of_iterators(A, B, C)
print(result)

result = sum_of_iterators2(A, B, C)
print(result)
