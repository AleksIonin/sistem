#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

# 7. Написать программу, которая считывает текст из файла и определяет, сколько в нем слов,
# состоящих из не менее чем семи букв. Необходимо
# реализовать сохранение и чтение данных из файла формата JSON.

if __name__ == '__main__':
    with open('text.json', 'r') as f:
        jtext = json.load(f)

    text = jtext['address'] # Получить одно из полей для поиска слов, длинее 6 букв

    # Удалить запятые.
    while "," in text:
        text = text.replace(",", "")

    # Разбить текст на слова.
    words = text.split(" ")

    # Подсчет слов, состоящих из не менее, чем семи букв
    word_count = 0
    output_json = dict()
    for word in words:
        if len(word) >=7:
            word_count += 1

    out = {"word_count": word_count} # создаем словарь для записи в файл

    # Запись в json файл
    with open("out.json", "w") as f:
        json.dump(out, f)

    print(f"Текст содержит {word_count} слов, которые состоят не менее, чем из 7 букв")
