__author__ = 'Узунов Дмитрий'

# Hard
#
# Задача-1 Пользователь вводит текст, необходимо разбить его по словам и
# выдать статистику по тексту
# 1. Сколько слов в тексте?
# 2. Сколько букв английского алфавита в тексте?
#

import string

text = input("Введите текст для анализа:")

text_for_letters = text_for_words = text

for i in string.punctuation:
    text_for_words = text_for_words.replace(i, "")

text_for_words = text_for_words.strip()

while "  " in text_for_words:
    text_for_words = text_for_words.replace("  ", " ")

words = text_for_words.split(" ")

print("Количество слов:", len(words))

count = dict()

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
print(count)


for i in text_for_letters:
    if i not in srting.ascii_letters:
        text_for_letters = text_for_letters.replace(i, "")

print(len(text_for_letters))


# Задача-2 Пользователь вводит два текста, необходимо найти все слова, которые
# есть в обоих текстах. Без учета регистра


text_1 = input("Введите текст 1 для анализа:")

for i in string.punctuation:
    text_1 = text_1.replace(i, "")

text_1 = text_1.strip()

text_1 = text_1.lower()

while "  " in text_1:
    text_1 = text_1.replace("  ", " ")

words_1 = text_1.split(" ")


text_2 = input("Введите текст 2 для анализа:")

for i in string.punctuation:
    text_2 = text_2.replace(i, "")

text_2 = text_2.strip()

text_2 = text_2.lower()

while "  " in text_2:
    text_2 = text_2.replace("  ", " ")

words_2 = text_2.split(" ")

print(set(words_1).intersection(set(words_2)))
