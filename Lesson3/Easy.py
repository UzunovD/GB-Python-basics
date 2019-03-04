__author__ = 'Узунов Дмитрий'

# EASY

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def user_round(numb, round_):
    '''
    Округляет произвольное десятичное число "numb", до кол-ва знаков
    "round"  по математическим правилам (0.6 --> 1, 0.4 --> 0)
    :param numb: float
    :param round_: int
    :return: float or int
    '''
    if type(numb) != float:
        print("TypeError: argument numb must be float")

    elif type(round_) != int:
        print("TypeError: argument round_ must be int")

    elif round_ < 0:
        print("ValueError: round_ must be >= 0")

    elif round_ == 0:
        decimal = numb % 1  # получаем дробную часть числа

        if decimal >= 0.5:
            numb = int(numb) + 1
        else:
            numb = int(numb)

    else:
        decimal = str(numb % 1)  # получаем дробную часть числа
        x = int(decimal[2 + round_])  # берем число по которому округляем

        if x >= 5:
            # Собираем число: целая часть+.+дробная часть до указанного
            #  разряда, увеличенная на 1
            numb = float(str(int(numb)) + "." + str(int(decimal[2: 2 + round_])
                                                    + 1))
        else:
            numb = float(str(int(numb)) + "." + str(int(decimal[2:2 + round_]
                                                        )))
    return numb


#
# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky(ticket):
    '''
    Определяет, является ли билет счастливым. Билет считается счастливым, если
    сумма его трех первых и последних цифр равны. Номер билета шестизначный.
    :param ticket: int
    :return: boolean
    '''
    if type(ticket) != int:
        print("TypeError: argument ticket must be int")
    elif len(str(ticket)) != 6:
        print("ValueError: ticket must consist of 6 numbers")

    else:
        luck = True

        ticket = list(str(ticket))
        left = sum([int(i) for i in ticket[0:3]])
        right = sum([int(i)for i in ticket[3:6]])

        if left != right:
            luck = False
        return luck

