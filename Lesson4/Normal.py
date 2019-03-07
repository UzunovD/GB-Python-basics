__author__ = 'Узунов Дмитрий'


#NORMAL
# Задание-1:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.


# import random
#
# with open("numbers.txt", 'w', encoding='UTF-8') as f:
#     f.write(''.join([random.choice(list('123456789')) for i in range(2501)]))
#
# with open("numbers.txt", 'r', encoding='UTF-8') as f:
#     numb_list = list(f.read())
#     list_int = []
#     list_same = []
#     max_len = []
#     for i in numb_list:
#         list_int.append(int(i))
#     j = 0
#     while j < len(list_int[:-1]):
#         if list_int[j] == list_int[j + 1]:
#             list_same.append(list_int[j])
#             if len(list_same) > len(max_len):
#                 max_len = list_same.copy()
#         j += 1
#     print(max_len)





# Задание-2
# Сформировать квадратную матрицу, в каждой строке которой находится ровно один
# ноль на случайном месте, остальные элементы тоже рандомные.
# Пользователь вводит размер


import random
import pprint

i = int(input("Введите число строк: "))
j = int(input("Введите число столбцов: "))
matrix = []

for row in range(i):
    row = []
    for el in range(j):
        row.append(random.randint(0,99))
    row[random.randint(0,4)] = 0
    matrix.append(row)

pprint.pprint(matrix)

