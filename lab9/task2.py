#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# lab 9 task2
# 6. Создать класс Triad (тройка чисел); определить методы изменения полей и вычисления
# суммы чисел. Определить производный класс Triangle с полями-сторонами. Определить
# методы вычисления углов и площади треугольника.


from math import acos
from math import degrees
from math import sqrt
import sys


class Triad:
    def __init__(self, num1, num2, num3):
        self.__first_num = num1
        self.__second_num = num2
        self.__third_num = num3

    @property
    def first_num(self):
        return self.__first_num

    @first_num.setter
    def first_num(self, w):
        if w > 0:
            self.__first_num = w
        else:
            raise ValueError

    @property
    def second_num(self):
        return self.__second_num

    @second_num.setter
    def second_num(self, w):
        if w > 0:
            self.__second_num = w
        else:
            raise ValueError

    @property
    def third_num(self):
        return self.__third_num

    @third_num.setter
    def third_num(self, w):
        if w > 0:
            self.__third_num = w
        else:
            raise ValueError

    # Вычислить сумму чисел
    def get_sum(self):
        return(self.__first_num + self.__second_num + self.__third_num)


class Triangle(Triad):
    def __init__(self, first_num, second_num, third_num):
        super().__init__(first_num, second_num, third_num)

    # Вычислить площадь треугольника
    def get_area(self):
        p = self.get_sum()/2
        pa = p - self.first_num
        pb = p - self.second_num
        pc = p - self.third_num
        return sqrt(p * pa * pb * pc)

    # Пересчет углов треугольника по его сторонам
    def calc(self):
        try:
            self.__ang_ab = degrees(acos((self.third_num ** 2 - self.first_num ** 2 - self.second_num ** 2)/(-2 * self.first_num * self.second_num)))
            self.__ang_bc = degrees(acos((self.first_num ** 2 - self.second_num ** 2 - self.third_num ** 2)/(-2 * self.second_num * self.third_num)))
            self.__ang_ac = degrees(acos((self.second_num ** 2 - self.first_num ** 2 - self.third_num ** 2)/(-2 * self.first_num * self.third_num)))
            return True
        except Exception as e:
            return False

    # Вывод информации о треугольнике
    def display(self):
        print(f"Стороны треугольника: {self.first_num}, {self.second_num}, {self.third_num}")
        if self.calc():
            print(f"Углы треугольника: {self.__ang_ac}, {self.__ang_ab}, {self.__ang_bc}")
            print(f"Площадь треугольника {self.get_area()}")
            print(f"Периметр треугольника {self.get_sum()}")
        else:
            print("Невозможно построить треугольник с такими сторонами")

    def read(self):
        sides = input("Введите стороны треугольника через пробел ").split(" ")
        if len(sides) == 3:
            self.first_num = int(sides[0])
            self.second_num = int(sides[1])
            self.third_num = int(sides[2])
        else:
            print("Для создания нового треугольника необходимо задать три стороны")


if __name__ == '__main__':
    # Создаем экземпляр класса и инициализируем его начальными значениями
    a = Triangle(3, 4, 5)
    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'read':
            a.read()

        elif command == 'display':
            a.display()

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("read - задать новые стороны треугольника;")
            print("display - вывести информацию о треугольнике;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
