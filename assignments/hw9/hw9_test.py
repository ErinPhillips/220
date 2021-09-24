import random
import sys

import pytest
from graphics import GraphWin, Point, Rectangle, Text

from hw9.button import Button
from tests.test_framework import Test_Framework as Tester

tester = Tester(sub_points=1)

win = GraphWin("Three Door Game", 600, 600)


class TestClass:

    def test_button(self):
        global tester
        global win
        tester.area_start("button tests")

        LABEL = "OK"
        rec_point_a = Point(1, 2)
        rec_point_b = Point(3, 4)
        rec = Rectangle(rec_point_a, rec_point_b)

        # Test Constructor
        tester.section("constructor")
        my_button = None
        try:
            my_button = Button(rec, LABEL)
            tester.run_test(True, True, "initialize constructor")
        except Exception as e:
            print('\nFAILED: Could not initialize Button, no more test will run.')
            sys.exit(1)
        tester.section_end()

        # test instance variables
        tester.section("instance variables")
        # shape
        tester.run_test(type(my_button.shape), Rectangle, "instance variable shape")
        # text
        tester.run_test(type(my_button.text), Text, "instance variable text")
        tester.section_end()

        # test methods
        tester.section("methods")
        # get_label
        tester.run_test(my_button.get_label(), LABEL, "get_label")
        # draw
        my_button.draw(win)
        tester.run_test(win.items[0], rec, "draw rectangle")
        tester.run_test(win.items[1].getText(), LABEL, "draw text")
        # undraw
        my_button.undraw()
        tester.run_test(len(win.items), 0, "undraw")
        # is_clicked
        is_clicked_values = build_is_clicked_tests(rec_point_a, rec_point_b)
        for test in is_clicked_values:
            is_clicked = my_button.is_clicked(test[0])
            tester.run_test(is_clicked, test[1], "click test", {'click point': test[0], 'button dimensions': (
                my_button.shape.getP1(), my_button.shape.getP2())})
        # color_button
        for color in get_colors():
            my_button.color_button(color)
            tester.run_test(my_button.shape.config["fill"], color, 'color button')
        # set_label
        for label in get_colors():
            my_button.set_label(label)
            tester.run_test(my_button.text.getText(), label, 'set label')
        tester.section_end()
        tester.area_end("button tests")

    def test_linter_button(self):
        global tester
        tester.area_start("code style | button")
        tester.lint('button.py', 12)
        tester.area_end("code style | button")

    def test_linter_game(self):
        global tester
        tester.area_start("code style | game")
        tester.lint('three_door_game.py', 10)
        tester.area_end("code style | game")

    @pytest.fixture(scope='session', autouse=True)
    def summary(self):
        yield
        tester.end_test(60)


def build_is_clicked_tests(pointA: Point, pointB: Point):
    ax = pointA.getX()
    ay = pointA.getY()
    bx = pointB.getX()
    by = pointB.getY()
    results = []
    for i in range(5):
        randX = random.randint(ax, bx)
        randY = random.randint(ay, by)
        results.append((Point(randX, randY), True))
    for i in range(5):
        randX = random.randint(0, ax - 1)
        randY = random.randint(0, ay - 1)
        results.append((Point(randX, randY), False))
    for i in range(5):
        randX = random.randint(bx + 1, bx + 50)
        randY = random.randint(by + 1, by + 50)
        results.append((Point(randX, randY), False))
    return results


def get_colors():
    return ["green", "red", "purple", "violet", "orange", "yellow", "thetimehascome", "blue"]
