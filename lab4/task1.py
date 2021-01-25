#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#lab 4-1
# 26. Дано предложение. Определить, сколько в нем гласных букв.

if __name__ == '__main__':
    sentence = input("Введите любую фразу на русском языке ")
    vowels = 0
    for i in sentence:
        letter = i.lower()
        if letter == "а" or letter == "е" or \
            letter == "ё" or letter == "о" or \
            letter == "и" or letter == "у" or \
            letter == "я" or letter == "ы" or \
            letter == "э" or letter == "ю":
            vowels += 1
    print(f"Фраза содержит {vowels} гласных звуков")

