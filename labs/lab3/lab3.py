"""
Erin Phillips
lab3.py
"""


def average():
    print("This program will calculate the average of your grades. ")
    hw = eval(input("Enter the number of grades you want to average: "))
    acc = 0
    for i in range(hw):
        grade = eval(input("Enter your grade on hw " + str(i + 1) + ": "))
        acc = acc + grade
        avg = acc / hw
        print(avg)


average()


def tip_jar():
    print("This program calculates the amount in a tip jar. ")
    acc = 0
    for i in range(5):
        amt = eval(input("Enter the donation amount: "))
        acc = acc + amt
        print(acc)


tip_jar()


def newton():
    print("This program approximates the square root of an number. ")
    x = eval(input("Enter the number you want to approximate the root of: "))
    refine = eval(input("Enter how many times to improve the approximation: "))
    approx = x // 2
    for i in range(refine):
        approx = (approx + (x / approx)) / 2

    print(approx)


newton()


def sequence():
    print("This program prints a series. ")
    x = eval(input("Enter the number of terms in the series: "))
    for i in range(1, x + 1):
        y = 1 + (i // 2 * 2)
        print(y, end=" ")
    print()


sequence()


def pi():
    print("This program approximates pi/2 using a series. ")
    terms = eval(input("Enter the number of terms in the series: "))
    acc = 1
    for i in range(terms):
        num = 2 + (i // 2 * 2)
        den = 1 + ((i + 1) // 2 * 2)
        frac = num / den
        acc = acc * frac

    print(acc * 2)


pi()
