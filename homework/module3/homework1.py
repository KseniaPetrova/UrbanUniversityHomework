# Пространство имен и способы вызова функции

"""
Задача("Однокоренные"):
Напишите функцию single_root_words, которая принимает одно обязательное слово в параметр root_word,
а далее неограниченную последовательность в параметр *other_words.
Функция должна составить новый список same_words только из тех слов списка other_words, которые содержат
root_word или наоборот root_word содержит одно из этих слов. После вернуть список same_words в качестве
результата своей работы.

Пункты задачи:
Объявите функцию single_root_words и напишите в ней параметры root_world и *other_words.
Создайте внутри функции пустой список same_words, который пополнится нужными словами.
При помощи цикла for переберите предполагаемо подходящие слова.
Пропишите корректное относительно задачи условие, при котором добавляются слова в результирующий список same_words.
После цикла верните образованный функцией список same_words.
Вызовите функцию single_root_words и выведете на экран(консоль) возвращённое ей занчение.
Пример результата выполнения программы:
Исходный код:
result1 = single_root_words('rich', 'richiest, 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
Вывод на консоль:
['richiest', 'orichalcum', 'richies']
['Able', 'Disable']
Примечания:
При проверке наичлия одного слова в составе другого стоит учесть, что регистр символов не должен влиять
ни на что. ('Disablement' - 'Able')
В основном в этой задаче вам понадобятся методы строк: count() и lower()/upper().

"""


def single_root_words (root_word, *other_words):
    same_words = []
    for word in other_words:
        if type(word) is not str and type(root_word) is not str:
            print('parameters must be string')
    root_word = root_word.lower()
    for word in other_words:
        word_lower = word.lower()
        other_words = [word_lower]  # добавляет слово в список целиком
        for i in other_words:
            if root_word in i or i in root_word:
                same_words.append(i)

    return same_words


result1 = single_root_words('rich', 'Richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
# result3 = single_root_words('Disablement', 'Able', 'Mable', 2, 'Bagel')

print(result1)
print(result2)
# print(result3)

# Вариант решения 2. отрабатывает число в кортеже, но коряво
# def single_root_words (root_word, *other_words):
#     same_words = []
#     if all(isinstance(word, str) for word in other_words) and type(root_word) == str:
#         root_word = root_word.lower()
#         other_words = tuple(word.lower() for word in other_words)
#         for i in other_words:
#             if root_word in i or i in root_word:
#                 same_words.append(i)
#     else:
#         print('parameters must be string')
#     return same_words
#
#
# result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
# result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
# result3 = single_root_words('Disablement', 'Able', 'Mable', 2, 'Bagel')
#
# print(result1)
# print(result2)
# print(result3)

"""
Очень интересный порядок вывода в консоль:
# parameters must be string
# ['richiest', 'orichalcum', 'richies']
# ['able', 'disable']
# []
сначала выполнилась строчку result3 = ... и вывелась в консоль, а потом все принты по порядку
"""


"""вариант от учителя"""
# def single_root_words(root_word, *other_words):
#     same_words = [] # Список для хранения слов, удовлетворяющих условию
#     root_word = root_word.lower() # Приведение корневого слова к нижнему регистру
#
#     for word in other_words:
#         word = word.lower() # Приведение текущего слова к нижнему регистру
#         if root_word in word or word in root_word: # Проверкa условия
#             same_words.append(word) # Добавление слова в список
#     return same_words

