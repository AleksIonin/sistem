#lab 3-3


if __name__ == '__main__':
    pound = 453.592
    weight = int(input("Enter the weight in whole pounds "))
    for i in range(1, weight + 1):
        print(i, "pounds equals ", (i * pound)/1000, "kg")
