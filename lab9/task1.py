#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# lab 9 task1
# 4. Создать класс Triangle для представления треугольника. Поля данных должны включать
# углы и стороны. Требуется реализовать операции: получения и изменения полей данных,
# вычисления площади, вычисления периметра, вычисления высот, а также определения
# вида треугольника (равносторонний, равнобедренный или прямоугольный).

from math import acos
from math import degrees

class Triangle:
    def __init__(self, side_a, side_b, side_c):
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c
        self.__ang_ab = degrees(acos((self.__side_c ** 2 - self.__side_a ** 2 - self.__side_b ** 2)/(-2 * self.__side_a * self.__side_b)))
        self.__ang_bc = degrees(acos((self.__side_a ** 2 - self.__side_b ** 2 - self.__side_c ** 2)/(-2 * self.__side_b * self.__side_c)))
        self.__ang_ac = degrees(acos((self.__side_b ** 2 - self.__side_a ** 2 - self.__side_c ** 2)/(-2 * self.__side_a * self.__side_c)))

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

    @property
    def ang_ab(self):
        return self.__ang_ab

    @ang_ab.setter
    def ang_ab(self, w):
        if w > 0:
            self.__ang_ab = w
        else:
            raise ValueError

    @property
    def ang_bc(self):
        return self.__ang_bc

    @ang_bc.setter
    def ang_bc(self, w):
        if w > 0:
            self.__ang_bc = w
        else:
            raise ValueError

    @property
    def ang_ac(self):
        return self.__ang_ac

    @ang_ac.setter
    def ang_ac(self, w):
        if w > 0:
            self.__ang_ac = w
        else:
            raise ValueError

    def check_triangle(self):
        angl_sum = self.__ang_ac + self.__ang_bc + self.__ang_ab
        if angl_sum >= 179.9 and angl_sum <= 180.1:
            return True
        else:
            return False

a = Triangle(2, 2, 2)
print(a.side_a, a.side_b, a.side_c, a.ang_ac, a.ang_ab, a.ang_bc)
print(a.check_triangle())



