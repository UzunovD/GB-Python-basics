# Hard Задача-3
n = int(input("Введите n:"))
m = int(input("Введите m:"))
i = 1

while i <= n:
    if i % 2 != 0:
        print("AAABBB" * m)
    else:
        print("BBBAAA" * m)
    i += 1
