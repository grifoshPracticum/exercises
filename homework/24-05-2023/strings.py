# 3. Задача из реального собеседования (очень простая, на разогрев) - функция принимает строку и выдает тру,
# если строка является полиндромом (может читаться задом наперед) и фолс в другом случае. Например madam - true, mama - false

# def is_palindrome(word):
#     return word == word[::-1]
#
# print(is_palindrome("madam"))



# у нас было решение с сравнением строки и ее обратным отражением, но мы решили что оно в 99% случаев будет медленное
# и хотим сравнивать по-индексно. У тебя было решение, но оно не работало, давай обсудим
def is_palindrome(word):
    reversed_word = word[::-1]
    for i, element in enumerate(word):
        if element != reversed_word[i]:
            return False
    return True

print(is_palindrome("racecar"))