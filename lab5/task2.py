#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#lab 5-2
from functools import reduce


initlst = [int(i) for i in input('Введите список целых чисел через пробел ').split()]
indmax = initlst.index(max(initlst)) # Получаем индекс максимального числа
print(f"номер максимального элемента списка {indmax}.")
zeroelem = [i for i,d in enumerate(initlst) if d==0] # Плдучаем список индексов всех нулевых элементов
if len(zeroelem) > 1:
    x = zeroelem[0]
    y = zeroelem[1]
    mlt = reduce(lambda x, y: x*y, initlst[x+1:y])
    print(f"Произведение элементов списка, расположенных между первым и вторым нулевыми элементами: {mlt}")
else:
    print("Нельзя получить произведение элементов между нулевыми элементами списка")
print([x for i, x in enumerate(initlst) if not i%2] + [x for i, x in enumerate(initlst) if i%2])

