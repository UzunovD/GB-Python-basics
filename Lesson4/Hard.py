__author__ = 'Узунов Дмитрий'

# Выполнено по видеоразбору

# HARD

# Задание-1
# Куб состоит из n^3 прозрачных и непрозрачных элементарных кубиков. Имеется ли
# хотя бы один просвет по каждому из трех измерений?
# Если это так, вывести координаты каждого просвета. Куб задается трехмерной
# матрицей из 0 и 1.

import random

N = int(input("Введите размер матрици: "))

cube = [[[random.randint(0, 1) for k in range(N)] for j in range(N)] for i
        in range(N)]

import pprint

pprint.pprint(cube)

empty_row = [0] * N

# Просвет по строкам
for matr in cube:
    for row in matr:
        if row == empty_row:
            pass

# Просвет по столбцам
for matr in cube:
    for i in range(N):
        buf = []
        for j in range(N):
            buf.append(matr[j][i])
        if buf == empty_row:
            pass

# Просвет в глубину
for i in range(N):
    for j in range(N):
        buf = []
        for height in range(N):
            buf.append(cube[height][i][j])
        if buf == empty_row:
            pass

# Задание-2
# Дан pwd.txt с логинами и паролями. Найдите топ10 самых популярных паролей.
#

# Задание-3
# Пользователь вводит положительное целое число больше 1
# Нужно создать квадратную матрицу этого размера и по спирали заполнить её
# числами

# 5
#  1  2  3  4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9

# 3
# 1 2 3
# 8 9 4
# 7 6 5
