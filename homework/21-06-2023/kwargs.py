# 1. напиши функцию, которая принимает сколько угодно параметров и превращает их в словарь.
# Вот ниже - только 3 заранее определнных параметра, а мы хотим сколько угодно

def dict_maker(name, salary, city):
    return {
        'name': name,
        'salary': salary,
        'city': city
    }


print(dict_maker(name='Anna', salary=200, city='Berlin'))


# 2. Напиши функцию которая принимает словарь и печатает его значения в формате. Сколько полей, столько и строк вывода
# Key1: <key>, value: <value>.
# Key2: <key>, value: <value>.



