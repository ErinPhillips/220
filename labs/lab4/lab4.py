"""
Erin Phillips
lab4.py
"""

from math import *
from graphics import *


def squares():
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    num_clicks = 5

    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)

    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setOutline("pink")
    shape.setFill("pink")
    shape.draw(win)

    for i in range(num_clicks):
        p = win.getMouse()
        shape = Rectangle(Point(p.getX() - 10, p.getY() - 10), Point(p.getX() + 10, p.getY() + 10))
        shape.setOutline("pink")
        shape.setFill("pink")
        shape.draw(win)

    instructions.setText("Click again to quit")
    win.getMouse()
    win.close()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Display the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """

    width = 400
    height = 400
    win = GraphWin("Rectangle", width, height)

    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click the opposite corners of the rectangle")
    instructions.draw(win)

    p1 = win.getMouse()
    p2 = win.getMouse()
    shape = Rectangle(p1, p2)
    shape.setOutline("pink")
    shape.setFill("pink")
    shape.draw(win)

    rect_length = abs(p1.getX() - p2.getX())
    rect_width = abs(p1.getY() - p2.getY())
    area = rect_length * rect_width
    perimeter = (rect_length * 2) + (rect_width * 2)

    area_pt = Point(width / 2, height - 30)
    area_text = Text(area_pt, "The area is: " + str(area))
    area_text.draw(win)

    perimeter_pt = Point(width / 2, height - 50)
    perimeter_text = Text(perimeter_pt, "The perimeter is: " + str(perimeter))
    perimeter_text.draw(win)

    instructions.undraw()
    instructions.setText("Click to quit")
    instructions.draw(win)

    win.getMouse()
    win.close()

rectangle()


def circle():
    width = 400
    height = 400
    win = GraphWin("Circle", width, height)

    p1 = win.getMouse()
    p2 = win.getMouse()
    x1 = p1.getX()
    x2 = p2.getX()
    y1 = p1.getY()
    y2 = p2.getY()
    radius = ((x2 - x1) ** 2 + (y2 - y1) ** 2)
    radius = sqrt(radius)
    shape = Circle(p1, radius)
    shape.setOutline("pink")
    shape.setFill("pink")
    shape.draw(win)

    radius_pt = Point(width / 2, height - 25)
    radius_text = Text(radius_pt, "The radius is: " + str(radius))
    radius_text.draw(win)

    instructions_pt = Point(width / 2, height - 50)
    instructions_text = Text(instructions_pt, "Click to quit")
    instructions_text.draw(win)

    win.getMouse()
    win.close()


circle()


def pi2():
    n = eval(input("Enter the number of terms to sum: "))
    acc = 0
    for i in range(n):
        num = 4
        denom = 1 + 2 * i
        frac = (num / denom) * ((-1) ** i)
        acc = acc + frac
    print(pi - acc)


pi2()
