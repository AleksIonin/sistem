#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#lab 3-3
# 6. Напечатать таблицу соответствия между весом в фунтах и весом в кг для значений от 1 до а
# фунтов с шагом 1 фунт, если 1 фунт = 400 г.


if __name__ == '__main__':
    pound = 453.592
    weight = int(input("Enter the weight in whole pounds "))
    for i in range(1, weight + 1):
        print(i, "pounds equals ", (i * pound)/1000, "kg")
