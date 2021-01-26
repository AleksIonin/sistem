#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# lab 9 task1
# 4. Создать класс Triangle для представления треугольника. Поля данных должны включать
# углы и стороны. Требуется реализовать операции: получения и изменения полей данных,
# вычисления площади, вычисления периметра, вычисления высот, а также определения
# вида треугольника (равносторонний, равнобедренный или прямоугольный).

from math import acos
from math import degrees
from math import sqrt

class Triangle:
    def __init__(self, side_a, side_b, side_c):
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c

    @property
    def side_a(self):
        return self.__side_a

    @side_a.setter
    def side_a(self, w):
        if w > 0:
            self.__side_a = w
        else:
            raise ValueError

    @property
    def side_b(self):
        return self.__side_b

    @side_b.setter
    def side_b(self, w):
        if w > 0:
            self.__side_b = w
        else:
            raise ValueError

    @property
    def side_c(self):
        return self.__side_c

    @side_c.setter
    def side_c(self, w):
        if w > 0:
            self.__side_c = w
        else:
            raise ValueError

    # Вычислить периметр треугольника
    def get_perimeter(self):
        return(self.__side_a + self.__side_b + self.__side_c)

    # Вычислить площадь треугольника
    def get_area(self):
        p = self.get_perimeter()/2
        pa = p - self.__side_a
        pb = p - self.__side_b
        pc = p - self.__side_c
        return sqrt(p * pa * pb * pc)

    # Вычислить высоты треугольника
    def get_heights(self):
        ha = (2 * self.get_area())/self.__side_a
        hb = (2 * self.get_area())/self.__side_b
        hc = (2 * self.get_area())/self.__side_c
        return ha, hb, hc

    # Определение вида треугольника
    def triangle_type(self):
        if self.__side_a == self.__side_b == self.__side_c:
            print("Равносторонний треугольник")
        elif self.__side_a == self.__side_b or self.__side_a == self.__side_c or self.__side_b == self.__side_c:
            print("Равнобедренный треугольник")
        if self.__ang_ac == 90 or self.__ang_ab == 90 or self.__ang_bc == 90:
            print("Прямоугольный треугольник")

    # Пересчет углов треугольника по его сторонам
    def calc(self):
        try:
            self.__ang_ab = degrees(acos((self.__side_c ** 2 - self.__side_a ** 2 - self.__side_b ** 2)/(-2 * self.__side_a * self.__side_b)))
            self.__ang_bc = degrees(acos((self.__side_a ** 2 - self.__side_b ** 2 - self.__side_c ** 2)/(-2 * self.__side_b * self.__side_c)))
            self.__ang_ac = degrees(acos((self.__side_b ** 2 - self.__side_a ** 2 - self.__side_c ** 2)/(-2 * self.__side_a * self.__side_c)))
            return True
        except Exception as e:
            return False

    # Вывод информации о треугольнике
    def output(self):
        print(f"Стороны треугольника: {a.side_a}, {a.side_b}, {a.side_c}")
        if self.calc():
            print(f"Углы треугольника: {a.__ang_ac}, {a.__ang_ab}, {a.__ang_bc}")
            print(f"Площадь треугольника {self.get_area()}")
            print(f"Периметр треугольника {self.get_perimeter()}")
            print(f"Высоты сторон треугольника {self.get_heights()}")
            self.triangle_type()
        else:
            print("Невозможно построить треугольник с такими сторонами")

# Создаем экземпляр класса
a = Triangle(1, 1, 100)
# Выводим информацию о треугольнике
a.output()

# Переопределяем стороны треугольника
a.side_a = 2
a.side_b = 2
a.side_c = 2

# Выводим информацию о треугольнике
a.output()

# Переопределяем стороны треугольника
a.side_a = 3
a.side_b = 4
a.side_c = 5

# Выводим информацию о треугольнике
a.output()
