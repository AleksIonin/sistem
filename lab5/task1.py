#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#lab 5-1
# 1. Ввести список А из 10 элементов, найти наибольший элемент и переставить его с первым
# элементом. Преобразованный массив вывести.

initlst = [int(i) for i in input('Введите список из 10 чисел через пробел ').split()]
i = initlst.index(max(initlst)) # Получаем индекс максимального числа
initlst[0], initlst[i] = initlst[i], initlst[0] # Меняем местами с первым
print(initlst)
