__author__ = 'Узунов Дмитрий'


# NORMAL

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def range_fib(n, m):
    '''
    Возвращаюет ряд Фибоначчи с n-элемента до m-элемента.
    Первыми элементами ряда считаются цифры 0 1 1
    :param n: int
    :param m: int
    :return: list(range_fib)
    '''

    p = 1
    q = 1
    range_fib = []

    if type(n) != int and type(m) != int:
        print("TypeError: argument must be int")

    elif n == 0:
        range_fib.append(0)
        for i in range(2):
            range_fib.append(1)
            continue

    elif n == 1:
        for i in range(2):
            range_fib.append(1)
            continue

    elif n == 2:
        range_fib.append(1)

    for i in range(3, m + 1):
        fib = p + q
        p = fib - p
        q = fib
        if 2 < i >= n:
            range_fib.append(fib)

    return range_fib

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def user_sort(s):
    '''
    Cортирует принимаемый список по возрастанию по средством пузырькового
    алгоритма.
    :param s: list
    :return: s[sorted in ascending order]
    '''

    for i in range(len(s) - 1):
        for j in range(len(s) - 1):
            if s[j] > s[j + 1]:
                s[j], s[j + 1] = s[j + 1], s[j]
    return s


