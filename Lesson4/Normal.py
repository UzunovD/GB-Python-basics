__author__ = 'Узунов Дмитрий'


#NORMAL
# Задание-1:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.


import random

with open("numbers.txt", 'w', encoding='UTF-8') as f:
    f.write(''.join([random.choice(list('123456789')) for i in range(2501)]))

with open("numbers.txt", 'r', encoding='UTF-8') as f:
    numb_str = f.read()
    list_temp = []
    list_same = []
    strin = ""
    j = 0

    while j < len(numb_str[:-1]):
        if numb_str[j] == numb_str[j + 1]:  #  Ищем начало последовательности
            while numb_str[j] == numb_str[j + 1]:  #  Пока есть последоват-сть
                list_temp.append(numb_str[j])  #  добавляем одинаковые цыфры
                strin = ''.join(list_temp)  #  сливаем в строку, чтобы добавить
                j += 1                      #  потом в список
            list_same.append(strin)         #  добавляем строку посл. в список
            list_temp = []                  #  обнуляем временный список
        j += 1

    max_same = ""
    for i in list_same:
        if len(i) > len(max_same):
            max_same = i

    print(max_same)





Задание-2
Сформировать квадратную матрицу, в каждой строке которой находится ровно один
ноль на случайном месте, остальные элементы тоже рандомные.
Пользователь вводит размер


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



