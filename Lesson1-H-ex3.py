# Hard Задача-3
n = int(input("Введите n:"))
m = int(input("Введите m:"))
i = 0

while i < n:
    if i % 2 != 0:
        print("BBBAAA" * m)
    else:
        print("AAABBB" * m)
    i += 1
