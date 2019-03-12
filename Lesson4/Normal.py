__author__ = 'Узунов Дмитрий'


# NORMAL
# Задание-1:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

def get_random_nubers(length: int) -> str:
    import random

    return ''.join([random.choice(list('123456789')) for _ in range(length)])


def get_longest_sequence(numbers: str) -> str:
    list_temp = []
    list_same = []
    j = 0

    while j < len(numbers[:-1]):
        if numbers[j] == numbers[j + 1]:  # Ищем начало последовательности
            while numbers[j] == numbers[j + 1]:  # Пока есть последоват-сть
                list_temp.append(numbers[j])  # добавляем одинаковые цыфры
                str_temp = ''.join(list_temp)  # сливаем в строку, чтобы
                j += 1  # добавить потом в список
            list_same.append(str_temp)  # добавляем строку последов. в список
            list_temp = []  # обнуляем временный список
        j += 1

    max_same = ""  # выбираем самую длинную последов-ть
    for i in list_same:
        if len(i) > len(max_same):
            max_same = i

    return max_same


with open("numbers.txt", 'w', encoding='UTF-8') as f:
    nums = get_random_nubers(int(input("Введите длинну числа: ")))
    f.write(nums)
    print(get_longest_sequence(nums))

# Задание-2
# Сформировать квадратную матрицу, в каждой строке которой находится ровно один
# ноль на случайном месте, остальные элементы тоже рандомные.
# Пользователь вводит размер


# import pprint
# import random
#
# i = int(input("Введите число строк: "))
# j = int(input("Введите число столбцов: "))
# matrix = []
#
# for row in range(i):
#     row = []
#     for el in range(j):
#         row.append(random.randint(0, 99))
#     row[random.randint(0, j - 1)] = 0  # вставляем в строку 0 рандомно
#     matrix.append(row)
#
# pprint.pprint(matrix)
