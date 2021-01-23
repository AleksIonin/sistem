import math
number = 5
st_num = 190393

task1 = st_num % 36 + 1
print ("task 1 -", task1)

task2 = (math.pow(st_num, 2) + 2) % 28 + 1
print ("task 2 -", task2)

task3 = (math.pow(st_num, 2) + 3) % 28 + 1
print ("task 3 -", task3)
