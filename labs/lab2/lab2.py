"""
Erin Phillips
lab2.py
"""

import math


def sum_of_threes():
    upper_bound = eval(input("Enter the upper bound: "))
    acc = 0
    for i in range(0, upper_bound + 1, 3):
        acc = acc + i

    print(acc)


sum_of_threes()


def multiplication_table():
    for h in range(1, 11):
        for l in range(1, 11):
            print(h * l, end=" ")
        print()


multiplication_table()


def triangle_area():
    a = eval(input("Enter the length of side a: "))
    b = eval(input("Enter the length of side b: "))
    c = eval(input("Enter the length of side c: "))
    s = (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    print(area)


triangle_area()


def sum_squares():
    start = eval(input("Enter the start: "))
    end = eval(input("Enter the end: "))
    acc = 0
    for i in range(start, end + 1):
        acc = acc + i ** 2

    print(acc)


sum_squares()


def power():
    base = eval(input("Enter the base: "))
    exp = eval(input("Enter the exponent: "))
    acc = 1
    for i in range(exp):
        acc = acc * base

    print(acc)


power()
