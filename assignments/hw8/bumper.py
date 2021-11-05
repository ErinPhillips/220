"""
Name: Erin Phillips
bumper.py

Problem: This program graphically simulates a system for an amusement park ride.

Certificate of Authenticity
I certify that this assignment is entirely my own work.
"""

from math import sqrt
from time import sleep
from random import randint
from graphics import GraphWin, Circle, Point, color_rgb


# generate a random color - return color
def get_random_color():
    red = randint(0, 256)
    green = randint(0, 256)
    blue = randint(0, 256)
    return color_rgb(red, green, blue)


# generate a random integer - return integer
def get_random(move_amount):
    return randint(-move_amount, move_amount)


# test if balls collide using distance formula - return boolean
def did_collide(ball1, ball2):
    center1 = ball1.getCenter()
    center2 = ball2.getCenter()
    radius_sum = ball1.getRadius() + ball2.getRadius()
    distance = sqrt((center1.getX() - center2.getX()) ** 2
                    + (center1.getY() - center2.getY()) ** 2)
    if distance <= radius_sum:
        return True
    return False


# test if a ball hits a vertical wall - return boolean
def hit_vertical(ball, win):
    center = ball.getCenter()
    radius = ball.getRadius()
    x_value = center.getX()
    v_wall = win.getWidth()
    if x_value <= radius:
        return True
    if x_value + radius >= v_wall:
        return True
    return False


# test if a ball hits a horizontal wall - return boolean
def hit_horizontal(ball, win):
    center = ball.getCenter()
    radius = ball.getRadius()
    y_value = center.getY()
    h_wall = win.getHeight()
    if y_value <= radius:
        return True
    if y_value + radius >= h_wall:
        return True
    return False


# move balls - dependent on return of boolean values
def move(ball1, ball2, win):
    dx1 = get_random(5)
    dy1 = get_random(7)
    dx2 = get_random(6)
    dy2 = get_random(8)
    while True:
        ball1.move(dx1, dy1)
        ball2.move(dx2, dy2)
        if hit_horizontal(ball1, win):
            dy1 = -dy1
        if hit_vertical(ball1, win):
            dx1 = -dx1
        if hit_horizontal(ball2, win):
            dy2 = -dy2
        if hit_vertical(ball2, win):
            dx2 = -dx2
        if did_collide(ball1, ball2):
            dx1 = -dx1
            dy1 = -dy1
            dx2 = -dx2
            dy2 = -dy2
        sleep(.01)


def main():
    height = 400
    width = 400
    win = GraphWin("Bumper", width, height)
    ball1 = Circle(Point(width / 2, height / 2), 15)
    ball2 = Circle(Point(width / 4, height / 4), 15)
    ball1.setFill(get_random_color())
    ball2.setFill(get_random_color())
    ball1.draw(win)
    ball2.draw(win)

    move(ball1, ball2, win)


if __name__ == '__main__':
    main()
