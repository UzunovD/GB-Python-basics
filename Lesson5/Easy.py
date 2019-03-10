__author__ = 'Узунов Дмитрий'

# EASY
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
# Учесть проверку на то что папка не пуста и на то, что такая папка уже существует

import os

# 1 script
for i in range(1, 10):

    name = "dir_" + str(i)

    if not os.path.exists(name):
        os.mkdir(name)
    else:
        print(f"Директория {name} уже существует")

# 2 script
for i in range(1, 10):

    name = "dir_" + str(i)

    if os.path.isdir(name):
        if os.listdir(name) == []:
            os.rmdir(name)
        else:
            print(f"Директория {name} не пуста")

# Задача-2:
# Напишите скрипт, который выводит в консоль список файлов и папок в указанной директории.

import os

print(os.listdir(input("Введите путь ")))
