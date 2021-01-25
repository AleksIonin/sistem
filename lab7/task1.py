#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 7. Написать программу, которая считывает текст из файла и определяет, сколько в нем слов,
# состоящих из не менее чем семи букв.

if __name__ == '__main__':
    with open('text.txt', 'r') as f:
        text = f.read()

    # Заменить символы в предложении.
    while "!" in text or "?" in text or "," in text or "." in text or ".." in text:
        text = text.replace("!", "")
        text = text.replace("?", "")
        text = text.replace(",", "")
        text = text.replace(".", "")
        text = text.replace("..", "")

    # Разбить текст на слова.
    words = text.split(" ")

    # Подсчет слов, состоящих из не менее, чем семи букв
    word_count = 0
    for word in words:
        if len(word) >=7:
            word_count += 1

    print(f"Текст содержит {word_count} слов, которые состоят не менее, чем из 7 букв")
