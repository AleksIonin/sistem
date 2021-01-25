#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

# Решить индивидуальное задание 2 лабораторной работы 7, оформив каждую команду в виде
# отдельной функции.
# 7. Написать программу, которая считывает текст из файла и определяет, сколько в нем слов,
# состоящих из не менее чем семи букв. Необходимо
# реализовать сохранение и чтение данных из файла формата JSON.


# Загрузить json файл и получить поле для поиска слов, длиннее 6 букв
def jload(fname):
    with open(fname, 'r') as f:
        jtext = json.load(f)
    text = jtext['address'] # Получить одно из полей для поиска слов, длинее 6 букв
    return text

def clean_text(raw_text):
    # Удалить запятые.
    text = ""
    while "," in raw_text:
        raw_text = raw_text.replace(",", "")
    return raw_text

def count_wt(cl_text):
    # Разбить текст на слова.
    words = cl_text.split(" ")

    # Подсчет слов, состоящих из не менее, чем семи букв
    word_count = 0
    output_json = dict()
    for word in words:
        if len(word) >=7:
            word_count += 1

    out = {"word_count": word_count} # создаем словарь для записи в файл
    return word_count, out

# Запись в json файл
def file_writing(source, filename):
    with open(filename, "w") as f:
        json.dump(source, f)

if __name__ == '__main__':
    # Получить одно из полей для поиска слов, длинее 6 букв
    rtext = jload('text.json')

    # Удалить запятые.
    text = clean_text(rtext)

    # Подсчет слов, состоящих из не менее, чем семи букв
    word_count, out = count_wt(text)

    # Запись в json файл
    file_writing(out, "out.json")

    print(f"Текст содержит {word_count} слов, которые состоят не менее, чем из 7 букв")
