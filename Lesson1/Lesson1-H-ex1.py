# Hard Задача-2
print("=Поиск числа из ряда Фибоначчи по номеру=")
n = int(input("Введите номер числа из ряда Фибоначчи:"))

i = 1
p = 1
q = 1
fib = 0
if n != 1 and n != 2:
    while i < n - 1:
        fib = p + q
        p = fib - p
        q = fib
        i += 1
    print("Для номера", n, "число Фибоначчи =", fib)
elif n == 1 or n == 2:
    print("Для номера", n, "число Фибоначчи =", 1)
