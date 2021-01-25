#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Lab 2
# 5. Даны длины сторон прямоугольного параллелепипеда. Найти его объем и площадь боковой
# поверхности.


length = float(input("Enter the length "))
width = float(input("Enter the width "))
height = float(input("Enter the height "))

print("The volume of a rectangular parallelepiped is", length * width * height)
print("The area of its lateral surface is", 2*(length+width)*height)
