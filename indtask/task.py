#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input("Введите натуральное число "))
r = n % 7
if r == 0:
    print("n = 7 * k")
else:
    print(f"n = 7 * k + {r}")

