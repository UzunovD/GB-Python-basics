# NORMAL Задача-1
print("=Определение максимальной цифры в числе=")
x = input("Введите произвольное целое число:")
m = 0

for a in x:
    while int(a) > m:
        m += 1
print(m)

# Альтернативаный вариант
x = input("Введите произвольное целое число:")
m = 0
i = 0

while i < len(x):
    while int(x[i]) > m:
        m += 1
    i += 1
print(m)
