# тривиальня задача на понимание синтаксиса
# напиши функцию которая принимает объект города и выдаем сумарный доходв всех


# def calculate_total_income(**kwargs):
#     population = kwargs.get('population', 0)
#     average_income = kwargs.get('av-income', 0)
#     total_income = population * average_income
#     return total_income
#
citi = {
    'population': 1_000_000,
    'av_income': 20_000,
    'name': 'Omsk'
}
#
# total_income = calculate_total_income(**citi)
# print("The total income of all residents in", citi['name'], "is:", total_income)


def calculate_total(population, av_income, **_rest): # '**_rest' - будут переданы все остальные аргументы и "утилизированы"
    return population*av_income

total_income = calculate_total(**citi)
print("The total income of all residents in", citi['name'], "is:", total_income)
