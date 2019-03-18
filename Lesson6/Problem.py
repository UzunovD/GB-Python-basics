__author__ = 'Узунов Дмитрий'


# Задача-1:
#
# Создать класс треугольник и реализовать в нем конструктор, методы для
# вычисления (не печати, нужен return) площади, периметра  и вывод значений
# сторон треугольника на экран.
# В конструкторе сделать проверку на возможность создания такого треугольника,
# если нет, то написать, что такой треугольник нельзя создать и сделать exit(1)

class Triangles:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        if self.a > self.c + self.b or self.b > self.a + self.c or self.c > \
                self.a + self.b:
            exit("Введены не допустимые аргументы")

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        return round(((self.perimeter() * (self.perimeter() - self.a) *
                       (self.perimeter() - self.b) * (self.perimeter()
                                                      - self.c)) ** 0.5), 2)


#
# Написать класс, который будет удобно использовать для работы с (на выбор
# что-нибудь одно) комплексными числами \ матрицами \ светофор \ микроволновка

