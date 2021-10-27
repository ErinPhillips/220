"""
Name: Erin Phillips
lab9.py
"""

from graphics import GraphWin, Circle, Text, Point
from math import sqrt


def add_ten(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def square_each(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sum_list(nums):
    acc = 0
    for i in range(len(nums)):
        acc = acc + nums[i]
    return acc


def to_numbers(str_list):
    for i in range(len(str_list)):
        str_list[i] = eval(str_list[i])


def write_sum_of_squares():
    file1 = input("Enter the name of the file: ")
    in_file = open(file1, 'r')
    out_file = open("output.txt", 'w')
    for line in in_file:
        new_line = line.split()
        to_numbers(new_line)
        square_each(new_line)
        sum_square = str(sum_list(new_line))
        print("Sum of squares = " + sum_square, file=out_file)


def starter():
    weight = float(input("Enter the weight: "))
    wins = int(input("Enter the number of wins: "))
    if 150 <= weight < 160 and wins >= 5:
        print("Player meets conditions!")
    elif weight > 199 and wins > 20:
        print("Player meets conditions!")
    else:
        print("The player does not meet conditions.")


def leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(year, "is a leap year!")
    else:
        print(year, "is not a leap year! sorry.")


def circle_overlap():
    win = GraphWin("Circle Overlap", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    radius1 = sqrt(((p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) ** 2))
    circle1 = Circle(p1, radius1)
    circle1.draw(win)
    p3 = win.getMouse()
    p4 = win.getMouse()
    radius2 = sqrt(((p3.getX() - p4.getX()) ** 2 + (p4.getY() - p4.getY()) ** 2))
    circle2 = Circle(p3, radius2)
    circle2.draw(win)
    distance = sqrt(((p1.getX() - p3.getX()) ** 2 + (p1.getY() - p3.getY()) ** 2))
    if distance < radius1 + radius2:
        message = Text(Point(200, 200), "The circles overlap.")
        message.draw(win)
    else:
        message = Text(Point(200, 200), "The circles do not overlap.")
        message.draw(win)

    win.getMouse()
    win.close()


def main():
    pass


main()
