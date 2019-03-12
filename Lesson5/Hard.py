__author__ = 'Узунов Дмитрий'

# HARD

# Написать программу для распаковки файлов в корневую из всех папок с
# расширениями (код взять с урока) и папки удалить

import os

PATH = input("Введите полный путь к каталогу: ")

dirs_path = []
for d in os.listdir(PATH):
    if os.path.isdir(os.path.join(PATH, d)):     # если папка
        dirs_path.append(os.path.join(PATH, d))  # общий список полных путей
                                                 # к папкам

for di in dirs_path:
    os.chdir(di)                                 # переходим в папку
    for f in os.listdir(di):                     # переименовываем файлы
        os.rename(os.path.join(di, f), os.path.join(os.path.split(di)[0], f))

os.chdir(PATH)                                   # переходим в корневую папку
dirs = os.listdir(PATH)
dirs_2 = dirs[:]
for i in dirs_2:                # если папка и эта папка пуста - удаляем папку
    if os.path.isdir(os.path.join(PATH, i)
                     ) and len(os.listdir(os.path.join(PATH, i))) == 0:
        os.rmdir(i)
