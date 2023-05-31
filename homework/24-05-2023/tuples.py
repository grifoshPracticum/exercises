# - напиши функцию которая превращает кортеж в число вот так: (1,2,7) => 127

# def tuple_to_int(my_tuple):
#     a = ""                                                                  # Плохо пахнет. Переделать.
#     for value in my_tuple:                                                  # У каждого числа есть разряд.
#         a += str(value)                                                     # Используй это для переделки
#     return int(a)
#
#
# print(tuple_to_int((1, 2, 7)))


def tuple_to_int2(my_tuple):
    result = 0
    multiplier = 1

    for digit in reversed(my_tuple):
        result += digit * multiplier
        multiplier *= 10

    return result

print(tuple_to_int2((1, 2, 7)))


# и еще одну которая делает обратно => 127 => (1,2,7)



# - напиши программу которая: принимает данных про людей - рост, вес, имя. данных таких - много, сотни тысяч...
# Вторая часть программы должна по весу и росту выдавать имена всех людей подходящих под критерий.
# Тут много концептов зарыто, поковыряй сам, может в несколько итераций обсудим.

# people_data = [
#         {'name': 'John', 'height': 180, 'weight': 75},
#         {'name': 'Alice', 'height': 165, 'weight': 60},
#         {'name': 'Bob', 'height': 175, 'weight': 80},
#         # Другие записи о людях...
#     ]
#
# def filter_people_by_criteria(people_data, height_threshold, weight_threshold):
#     filtered_people = []
#     for person in people_data:
#         if person['height'] >= height_threshold and person['weight'] <= weight_threshold:
#             filtered_people.append(person['name'])
#     return filtered_people