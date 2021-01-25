#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# lab 8
# Решить индивидуальное задание лабораторной работы 6, оформив каждую команду в виде
# отдельной функции.
# Задание из лабораторной работы 6:
# 2. Использовать словарь, содержащий следующие ключи: фамилия и инициалы; номер
# группы; успеваемость (список из пяти элементов). Написать программу, выполняющую
# следующие действия: ввод с клавиатуры данных в список, состоящий из словарей заданной
# структуры; записи должны быть упорядочены по возрастанию среднего балла; вывод на
# дисплей фамилий и номеров групп для всех студентов, имеющих оценки 4 и 5; если таких
# студентов нет, вывести соответствующее сообщение.

import sys

def data_add(students, estimates):
    # Запросить данные о работнике.
    name = input("Фамилия и инициалы? ")
    group_number = input("Номер группы? ")
    estimate = int(input(f"Успеваемость? Выберите одно из значений {estimates}"))

    # Создать словарь.
    student = {
        'name': name,
        'group_number': group_number,
        'estimate': estimate,
    }

    # Добавить словарь в список.
    students.append(student)
    # Отсортировать список в случае необходимости.
    if len(students) > 1:
        students.sort(key=lambda item: item.get('estimate', ''), reverse=True)

def data_list(students):
    # Заголовок таблицы.
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 12
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^12} |'.format(
            "No",
            "Ф.И.О.",

            "Номер группы",
            "Успеваемость"
        )
    )

    print(line)

    # Вывести данные о всех студентах.
    st_ex = False
    for idx, student in enumerate(students, 1):
        if student.get('estimate') >=4:
            st_ex = True
            print(
                '| {:>4} | {:<30} | {:<20} | {:>12} |'.format(
                    idx,
                    student.get('name', ''),
                    student.get('group_number', ''),
                    student.get('estimate', 0)
                )
            )
    if st_ex == False:
        print("Отсутствуют студенты с оценками 4 или 5")
    else:
        print(line)

def help():
    # Вывести справку о работе с программой.
    print("Список команд:\n")
    print("add - добавить студента;")
    print("list - вывести список студентов;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")

def unknown(command):
    print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    # Список студентов.
    students = []
    estimates = [1, 2, 3, 4, 5]

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            data_add(students, estimates)

        elif command == 'list':
            data_list(students)

        elif command == 'help':
            help()

        else:
            unknown(command)
