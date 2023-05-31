# Создай функцию для печати суммы чека. Функция принимает массив словарей c товарами
# и должна печатать что-то формата "Сумма чека 7 рублей"
# А теперь представь что тебе для разных стран надо писать разное: "рублей", "евро", "долларов" и так далее


GOODS = [
    {'name': 'bread',   'price': 1.00, 'quantity': 3, "currency": "USD"},
    {'name': 'milk',    'price': 2.00, 'quantity': 2, "currency": "USD"},
    {'name': 'gold',    'price': 8.00, 'quantity': 5, "currency": "USD"},
    {'name': 'silver',  'price': 2.00, 'quantity': 4, "currency": "USD"},
]


def create_print_receipt(currency):
    def print_receipt(list_of_goods):
        amount = 0
        for item in list_of_goods:
            amount += item['price'] * item['quantity']
        print(f"Сумма чека: {amount} {currency}")

    return print_receipt


print_receipt_usd = create_print_receipt("долларов")
print_receipt_usd(GOODS)

print_receipt_rub = create_print_receipt("рублей")
print_receipt_rub(GOODS)

# Попробуй использовать подход "функция возвращает функцию", если надо - на уроке дам подсказку.

# Еще у меня в моей ветке есть решение, покажу его тебе и сравним с тем что сделал ты
# Очень хорошая теория к материалу лежит тут (плавная подводка к теме декораторы):
# https://towardsdatascience.com/functions-that-return-functions-higher-order-functions-and-decorators-in-python-with-examples-4282742cdd3e
