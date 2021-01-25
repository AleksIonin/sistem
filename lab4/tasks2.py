#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#lab 4-2
# 24. Дано слово из четного числа букв. Поменять местами первую букву со второй, третью – с
# четвертой и т. д.

if __name__ == '__main__':
    word = input("Введите слово, состоящее из четного числа букв ")
    if len(word) % 2 == 1:
        print("Длина слова нечетная")
    else:
        s = list(word)
        for i in range(0, len(s), 2):
            t = s[i]
            s[i] = s[i+1]
            s[i+1] = t

        print("".join(s))
