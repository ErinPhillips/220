"""
Name: Erin Phillips
Lab5.py
"""

from graphics import *
from math import sqrt


def target():
    w = 500
    l = 500
    win = GraphWin("Archery Target", l, w)
    r = w / 10
    circle = Circle(Point(250, 250), 5 * r)
    circle.setFill('white')
    circle.draw(win)
    circle = Circle(Point(250, 250), 4 * r)
    circle.setFill('black')
    circle.draw(win)
    circle = Circle(Point(250, 250), 3 * r)
    circle.setFill('blue')
    circle.draw(win)
    circle = Circle(Point(250, 250), 2 * r)
    circle.setFill('red')
    circle.draw(win)
    circle = Circle(Point(250, 250), r)
    circle.setFill('yellow')
    circle.draw(win)

    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    message = Text(Point(350, 450), "Click on three points")
    message.draw(win)

    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()
    shape = Polygon(p1, p2, p3)
    shape.setFill("pink")
    shape.setOutline("pink")
    shape.draw(win)

    a = sqrt((p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) ** 2)
    b = sqrt((p2.getX() - p3.getX()) ** 2 + (p2.getY() - p3.getY()) ** 2)
    c = sqrt((p3.getX() - p1.getX()) ** 2 + (p3. getY() - p1.getY()) ** 2)
    perimeter = round(a + b + c, 2)
    s = perimeter / 2
    area = round(sqrt(s * (s - a) * (s - b) * (s - c)), 2)

    message.setText("The perimeter is: " + str(perimeter))
    area_txt = Text(Point(350, 400), "The area is: " + str(area))
    area_txt.draw(win)

    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    red_box = Entry(Point(win_width / 2 + 2, win_height / 2 + 40), 5)
    green_box = Entry(Point(win_width / 2 + 2, win_height / 2 + 70), 5)
    blue_box = Entry(Point(win_width / 2 + 2, win_height / 2 + 100), 5)

    red_box.draw(win)
    green_box.draw(win)
    blue_box.draw(win)

    for i in range(5):
        win.getMouse()
        red = int(red_box.getText())
        green = int(green_box.getText())
        blue = int(blue_box.getText())
        color = color_rgb(red, green, blue)
        shape.setFill(color)

    win.getMouse()
    win.close()


def process_string():
    s = input("Enter  a string: ")
    print(s[0])
    print(s[len(s) - 1])
    print(s[2:6])
    print(s[0] + s[len(s) - 1])
    print(s[0:3] * 10)
    for i in range(len(s)):
        c = s[i]
        print(c)
    print(len(s))


def process_list():
    pt = Point(5, 10)
    values = [5, 'hi', 2.5, 'there', pt, '7.2']
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = 5 * values[1]
    print(x)
    x = values[2:5]
    print(x)
    x = [values[2], values[3], values[0]]
    print(x)
    x = [values[2], values[0], float(values[5])]
    print(x)
    x = values[2] + values[0] + float(values[5])
    print(x)
    x = len(values)
    print(x)


def another_series():
    x = eval(input("Enter the number of terms: "))
    acc = 0
    for i in range(x):
        y = 2 + 2 * (i % 3)
        acc = acc + y
        print(y, end=' ')

    print()
    print("Sum = ", acc)


def main():
    target()
    triangle()
    color_shape()
    process_string()
    process_list()
    another_series()


main()
