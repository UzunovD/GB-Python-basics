# NORMAL Задача-3
import math
print("Программа вычисляет корни квадратного уравнения вида "
      "ax² + bx + c = 0.")
a = int(input("Введите коэффициент a="))
b = int(input("Введите коэффициент b="))
c = int(input("Введите коэффициент c="))

D = b**2 - 4*a*c

if D < 0:
    print("Уравнение не имеет корней")

else:
    x1 = (-b + math.sqrt(D))/(2*a)
    x2 = (-b - math.sqrt(D))/(2*a)

    print("x1 =", x1, "x2 =", x2,)
print("Окончание программы")
