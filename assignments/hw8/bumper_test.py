import json

from graphics import GraphWin, Circle, Point

from hw8 import bumper
from tests import api_service
from tests.hw7.test_case import TestCase
from tests.test_framework import *

total = 0
global_points = 5
sub_points = 1
code_style_points = 15
win = GraphWin("test", 600, 400)


class TestClass:

    def test_hw(self):
        builder = TestBuilder('Bumper', 'bumper.py', 15)
        static_tests = build_static_section()
        # dynamic_teses = build_dynamic_section()
        builder.add_items(static_tests)
        builder.run()


# static tests
def build_static_section():
    test_cases = TestCase()
    test_cases.did_collide_tests = [
        {'x1': 71, 'y1': 74, 'r1': 7, 'x2': 51, 'y2': 185, 'r2': 7, 'expected': False},
        {'x1': 36, 'y1': 54, 'r1': 29, 'x2': 10, 'y2': 47, 'r2': 29, 'expected': True},
        {'x1': 7, 'y1': 8, 'r1': 9, 'x2': 10, 'y2': 11, 'r2': 12, 'expected': True},
        {"x1": 87, "y1": 58, "r1": 20, "x2": 54, "y2": 100, "r2": 20, "expected": False},
        {"x1": 59, "y1": 97, "r1": 38, "x2": 75, "y2": 82, "r2": 38, "expected": True},
        {"x1": 97, "y1": 97, "r1": 42, "x2": 100, "y2": 1, "r2": 42, "expected": False}
    ]
    test_cases.get_random_tests = [10, 50, 100]
    test_cases.hit_vertical_tests = [
        {'x': 120, 'y': 116, 'radius': 35, 'expected': False},
        {'x': 19, 'y': 50, 'radius': 20, 'expected': True},
        {'x': 20, 'y': 50, 'radius': 20, 'expected': True},
        {'x': 21, 'y': 50, 'radius': 20, 'expected': False},
        {'x': 59, 'y': 50, 'radius': 40, 'expected': False},
        {'x': 560, 'y': 50, 'radius': 40, 'expected': True},
        {'x': 561, 'y': 50, 'radius': 40, 'expected': True}
    ]
    test_cases.hit_horizontal_tests = [
        {'x': 200, 'y': 40, 'radius': 10, 'expected': False},
        {'x': 50, 'y': 19, 'radius': 20, 'expected': True},
        {'x': 50, 'y': 20, 'radius': 20, 'expected': True},
        {'x': 50, 'y': 21, 'radius': 20, 'expected': False},
        {'x': 50, 'y': 59, 'radius': 40, 'expected': False},
        {'x': 50, 'y': 360, 'radius': 40, 'expected': True},
        {'x': 50, 'y': 361, 'radius': 40, 'expected': True}
    ]
    return run_test(test_cases, 'static tests')


# dynamic tests
def build_dynamic_section():
    response = api_service.test('hw7', 'GET',
                                params={'number': 13, 'width': win.getWidth(), 'height': win.getHeight()})
    api_tests = json.loads(response.text)
    test_cases = TestCase()
    test_cases.hit_vertical_tests = api_tests['hitVerticalTests']
    test_cases.hit_horizontal_tests = api_tests['hitHorizontalTests']
    test_cases.get_random_tests = api_tests['getRandomTests']
    test_cases.did_collide_tests = api_tests['didCollideTests']

    return run_test(test_cases, 'api tests')


def run_test(test_cases, test_type):
    section = Section(test_type)

    # DID COLLIDE TESTS
    collide_section = Section('did_collide()')
    for i, test in enumerate(test_cases.did_collide_tests):
        c1 = Circle(Point(test['x1'], test['y1']), test['r1'])
        c2 = Circle(Point(test['x2'], test['y2']), test['r2'])
        actual = bumper.did_collide(c1, c2)
        collide_section.add_items(Test(f'test {i}', actual, test['expected'], [c1, c2]))

    # GET RANDOM TESTS
    get_random_section = Section('get_random()')
    for j, test in enumerate(test_cases.get_random_tests):
        temp_actual = 0
        in_range = True
        fail_range_value = 0
        positive_in = False
        negative_in = False
        for i in range(700):
            temp_actual = bumper.get_random(test)
            if not (test * -1 <= temp_actual <= test):
                in_range = False
                fail_range_value = temp_actual
            if temp_actual == test:
                positive_in = True
            if temp_actual == test * -1:
                negative_in = True

        if not in_range:
            actual = fail_range_value
            expected = f'-{test} <= actual <= {test}'
        elif not positive_in:
            actual = f'after multiple tests, value {test} never returned'
            expected = f'should have seen {test} returned when called with argument {test}'
        elif not negative_in:
            actual = f'after multiple tests, value -{test} never returned'
            expected = f'should have seen -{test} returned when called with argument {test}'
        else:
            actual = f'-{test} <= {temp_actual} <= {test}'
            expected = f'-{test} <= {temp_actual} <= {test}'
        get_random_section.add_items(Test(f'test {j}', actual, expected))

    # HIT VERTICAL TESTS
    hit_vertical_section = Section('hit_vertical()')
    for i, test in enumerate(test_cases.hit_vertical_tests):
        expected = test['expected']
        circle = Circle(Point(test['x'], test['y']), test['radius'])
        data = (circle, win)
        actual = bumper.hit_vertical(circle, win)
        hit_vertical_section.add_items(Test(f'test {i}', actual, expected, data))

    # HIT HORIZONTAL TESTS
    hit_horizontal_section = Section('hit_horizontal()')
    for i, test in enumerate(test_cases.hit_horizontal_tests):
        expected = test['expected']
        circle = Circle(Point(test['x'], test['y']), test['radius'])
        data = (circle, win)
        actual = bumper.hit_horizontal(circle, win)
        hit_horizontal_section.add_items(Test(f'test {i}', actual, expected, data))

    section.add_items(collide_section, get_random_section, hit_vertical_section, hit_horizontal_section)
    return section
