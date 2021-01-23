#lab3-1


ex_num = int(input("Введите количество экзаменов от 1 до 20 "))
if ex_num == 1:
    print("Мы успешно сдали ", ex_num, "экзамен.")
elif (ex_num  >= 2) and (ex_num <= 4):
    print("Мы успешно сдали ", ex_num, "экзамена.")
elif ex_num > 4 and ex_num <= 20:
    print("Мы успешно сдали ", ex_num, "экзаменов.")
else:
    print("Введено недопустимое количество экзаменов")
