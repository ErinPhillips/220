"""
Name: Erin Phillips
threedoorgame.py

Problem: this program emulates a guessing game

Certificate of Authenticity
I certify that this assignment is entirely my own work.
"""

from graphics import *
from button import Button
from random import randint


def main():
    # creates window. draws buttons and prompts
    win = GraphWin("Three Door Game", 500, 300)
    p1, p2 = Point(50, 100), Point(150, 200)
    p3, p4 = Point(200, 100), Point(300, 200)
    p5, p6 = Point(350, 100), Point(450, 200)
    door1 = Button(Rectangle(p1, p2), "Door 1")
    door2 = Button(Rectangle(p3, p4), "Door 2")
    door3 = Button(Rectangle(p5, p6), "Door 3")

    prompt1 = Text(Point(250, 50), "I have a secret door...")
    prompt2 = Text(Point(250, 250), "Click to choose my door")

    door1.draw(win), door2.draw(win), door3.draw(win)
    prompt1.draw(win), prompt2.draw(win)

    # randomly generates secret door
    door_list = [door1, door2, door3]
    secret_door = door_list[randint(0, 2)]

    # wait for user click - store as guess
    guess = win.getMouse()

    # if user click is invalid (not on a door)
    # prompts to click again until valid click
    while not door1.is_clicked(guess) and not door2.is_clicked(guess)\
            and not door3.is_clicked(guess):
        prompt2.setText("Oops! Please click a door!")
        guess = win.getMouse()

    # game is won
    if secret_door.is_clicked(guess):
        secret_door.color_button("light green")
        prompt1.setText("You Win!")
        prompt2.setText("Click to close")

    # game is lost
    else:
        secret_door.color_button("Red")
        prompt1.setText("You Lost!")
        prompt2.setText(str(secret_door.get_label()) + " is my secret door")

    win.getMouse()


main()
