#lab3-2
import math

if __name__ == '__main__':
    m1x = int(input("Введите значение х1 "))
    m1y = int(input("Введите значение y1 "))
    m2x = int(input("Введите значение х2 "))
    m2y = int(input("Введите значение y2 "))

    if m1x == m2x and math.fabs(m1y) == math.fabs(m2y):
        print("Points M1 and M2 are symmetrical about the X axis")
    if m1y == m2y and math.fabs(m1x) == math.fabs(m2x):
        print("Points M1 and M2 are symmetrical about the Y axis")

