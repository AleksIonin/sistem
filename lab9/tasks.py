#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
number = 5
st_num = 190393

task1 = ((math.pow(st_num, 2)) + st_num +1) % 15 + 1
print ("task 1 -", task1)

task2 = ((math.pow(st_num, 2)) + st_num +3) % 20 + 1
print ("task 2 -", task2)
