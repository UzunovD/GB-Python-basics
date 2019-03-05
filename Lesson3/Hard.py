__author__ = 'Узунов Дмитрий'

# HARD

# Задание-1

# Написать консольное меню вида:

# 1. Добавить
# 2. Удалить
# 3. Распечатать
# 4. Посчитать
# 5. Выйти

# Надо чтобы
# а) Можно было удобно менять порядок меню и\или добавлять\удалять пункты меню
# б) Каждое действие (добавить, удалить и тд) должно быть функцией
# в) У пользователя надо спросить номер команды
# г) Программа не должна завершаться пока не введется команда Выйти
# д) Проверять на ввод ошибочных данных, там где они могут появиться

database = []


def add():
    global database

    data = input("Введите значение:")
    database.append(data)


def remove():
    global database

    for i, m in enumerate(database, start=1):
        print(f"{i}. {m}")

    i = int(input("Введите № пп который необходимо удалить: "))
    database.pop(i - 1)


def print_data():
    global database

    if len(database) == 0:
        print("Нет данных")

    for i, m in enumerate(database, start=1):
        print(f"{i}. {m}")


def count():
    print_operation(operation)

    count = int(input("Выберете операцию:"))

    return oper[count - 1]()


def sum_():
    global database

    for i, m in enumerate(database, start=1):
        print(f"{i}. {m}")
    arg1 = int(input("Введите № первого слогаемого: "))
    arg2 = int(input("Введите № второго слогаемого: "))

    print((int(database[arg1 - 1]) + int(database[arg2 - 1])))


def difer():
    global database

    for i, m in enumerate(database, start=1):
        print(f"{i}. {m}")

    arg1 = int(input("Введите № уменьшаемого: "))
    arg2 = int(input("Введите № вычитаемого: "))

    print(int(database[arg1 - 1]) - int(database[arg2 - 1]))


def mult():
    global database

    for i, m in enumerate(database, start=1):
        print(f"{i}. {m}")

    arg1 = int(input("Введите № первого множителя: "))
    arg2 = int(input("Введите № второго множителя: "))

    print(int(database[arg1 - 1]) * int(database[arg2 - 1]))


def div():
    global database

    for i, m in enumerate(database, start=1):
        print(f"{i}. {m}")

    arg1 = int(input("Введите № п частного: "))
    arg2 = int(input("Введите № п делителя: "))

    print(int(database[arg1 - 1]) / int(database[arg2 - 1]))


def exp():
    global database

    for i, m in enumerate(database, start=1):
        print(f"{i}. {m}")

    arg1 = int(input("Введите № п который необходимо возвести в квадрат: "))

    print(int(database[arg1 - 1]) * int(database[arg1 - 1]))


def square():
    global database

    for i, m in enumerate(database, start=1):
        print(f"{i}. {m}")

    arg1 = int(input("Введите № п из которого необходимо извлеч корень "
                     "квадратный: "))

    print(int(database[arg1 - 1]) ** 0, 5)


def print_menu(menu):
    for i, m in enumerate(menu, start=1):
        print(f"{i}. {m}")


def print_operation(operation):
    for i, m in enumerate(operation, start=1):
        print(f"{i}. {m}")


def get_command(menu):
    command = int(input("Введите команду: "))

    if 1 <= command <= len(menu):
        return command
    else:
        return -1


operation = ["+", "-", "*", "/", "**", "квадратный корень из числа"]
oper = [sum_, difer, mult, div, exp, square]
menu = ["Добавить", "Удалить", "Распечатать", "Посчитать", "Выйти"]
commands = [add, remove, print_data, count, exit]

while True:
    print()
    print_menu(menu)
    command = get_command(menu)

    if command == -1:
        print("Неверная команда!")
        continue

    commands[command - 1]()
