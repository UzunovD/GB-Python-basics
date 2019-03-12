__author__ = 'Узунов Дмитрий'

# HARD

# Написать программу для распаковки файлов в корневую из всех папок с
# расширениями (код взять с урока) и папки удалить

import os


PATH = input("Введите полный путь к каталогу: ")

dirs_path = []
for d in os.listdir(PATH):
    if os.path.isdir(os.path.join(PATH, d)):
        dirs_path.append(os.path.join(PATH, d))

for di in dirs_path:
    os.chdir(di)
    for f in os.listdir(di):
        os.rename(os.path.join(di, f), os.path.join(os.path.split(di)[0], f))

os.chdir(PATH)
dirs = os.listdir(PATH)
dirs_2 = dirs[:]
for i in dirs_2:
    if os.path.isdir(os.path.join(PATH, i)):
        os.rmdir(i)
