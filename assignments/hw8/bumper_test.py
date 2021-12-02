from graphics import Circle, Point

from hw8 import bumper
from tests.hw8 import random_tests
from tests.hw8.test_case import TestCase
from tests.test_framework import *


class MockWin:
    def __init__(self, width, height, *args, **kwargs):
        self.width = width
        self.height = height

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height


class TestClass:

    def test_hw(self):
        builder = TestBuilder('Bumper', 'bumper.py', 15)
        static_tests = build_static_section()
        dynamic_tests = build_dynamic_section()
        builder.add_items(static_tests, dynamic_tests)
        builder.run()


# static tests
def build_static_section():
    test_cases = TestCase()
    test_cases.did_collide_tests = [
        ({'x1': 63, 'y1': 85, 'r1': 42, 'x2': 62, 'y2': 93, 'r2': 2, 'expected': True}, True),
        ({'x1': 84, 'y1': 83, 'r1': 48, 'x2': 7, 'y2': 22, 'r2': 35, 'expected': False}, False),
        ({'x1': 96, 'y1': 95, 'r1': 39, 'x2': 98, 'y2': 36, 'r2': 37, 'expected': True}, True),
        ({'x1': 64, 'y1': 81, 'r1': 28, 'x2': 31, 'y2': 26, 'r2': 3, 'expected': False}, False),
        ({'x1': 90, 'y1': 87, 'r1': 13, 'x2': 93, 'y2': 88, 'r2': 6, 'expected': True}, True),
        ({'x1': 71, 'y1': 90, 'r1': 38, 'x2': 28, 'y2': 24, 'r2': 8, 'expected': False}, False)
    ]
    test_cases.get_random_tests = [10, 50, 100]
    test_cases.hit_vertical_tests = [
        {'radius': 59, 'x': 58, 'y': 78, 'expected': True, 'width': 384, 'height': 829},
        {'radius': 95, 'x': 534, 'y': 110, 'expected': False, 'width': 630, 'height': 159},
        {'radius': 92, 'x': 111, 'y': 35, 'expected': True, 'width': 202, 'height': 332},
        {'radius': 78, 'x': 158, 'y': 170, 'expected': False, 'width': 237, 'height': 356},
        {'radius': 55, 'x': 74, 'y': 252, 'expected': True, 'width': 128, 'height': 656},
        {'radius': 78, 'x': 79, 'y': 685, 'expected': False, 'width': 913, 'height': 971},
        {'radius': 8, 'x': 931, 'y': 205, 'expected': True, 'width': 938, 'height': 666},
    ]
    test_cases.hit_horizontal_tests = [
        {'radius': 16, 'x': 145, 'y': 15, 'expected': True, 'width': 181, 'height': 880},
        {'radius': 48, 'x': 124, 'y': 580, 'expected': False, 'width': 595, 'height': 629},
        {'radius': 8, 'x': 23, 'y': 12, 'expected': True, 'width': 274, 'height': 19},
        {'radius': 87, 'x': 283, 'y': 88, 'expected': False, 'width': 496, 'height': 782},
        {'radius': 100, 'x': 243, 'y': 99, 'expected': True, 'width': 577, 'height': 428},
        {'radius': 89, 'x': 7, 'y': 90, 'expected': False, 'width': 149, 'height': 278},
        {'radius': 40, 'x': 299, 'y': 318, 'expected': True, 'width': 455, 'height': 357},
    ]
    return run_test(test_cases, 'static tests')


# dynamic tests
def build_dynamic_section():
    dynamic_tests = random_tests.create(13)
    test_cases = TestCase()
    test_cases.hit_vertical_tests = dynamic_tests['hitVerticalTests']
    test_cases.hit_horizontal_tests = dynamic_tests['hitHorizontalTests']
    test_cases.get_random_tests = dynamic_tests['getRandomTests']
    test_cases.did_collide_tests = dynamic_tests['didCollideTests']

    return run_test(test_cases, 'dynamic tests')


def run_test(test_cases, test_type):
    section = Section(test_type)

    # DID COLLIDE TESTS
    collide_section = Section('did_collide()')
    for i, test_tup in enumerate(test_cases.did_collide_tests):
        test, t_or_f = test_tup
        not_var = '' if t_or_f else 'not '
        c1 = Circle(Point(test['x1'], test['y1']), test['r1'])
        c2 = Circle(Point(test['x2'], test['y2']), test['r2'])
        outcome, result = run_safe(lambda: bumper.did_collide(c1, c2))
        collide_section.add_items(Test(f'test {i} - did {not_var}collide', result, test['expected'], [c1, c2]))

    # GET RANDOM TESTS
    get_random_section = Section('get_random()')
    r = 2000
    for j, test in enumerate(test_cases.get_random_tests):
        # in range
        in_range = True
        fail_value = 0
        error = False
        res = 0
        for i in range(r):
            outcome, res = run_safe(lambda: bumper.get_random(test))
            if not outcome:
                error = True
                fail_value = res
                break
            if res > test or res < test * -1:
                in_range = False
                fail_value = res
                break
        if error or not in_range:
            get_random_section.add_items(Test(f'in range test {j}', fail_value, f'between -{test} and {test}'))
        else:
            get_random_section.add_items(
                Test(f'in range test {j}', f'{res} between -{test} and {test}', f'{res} between -{test} and {test}'))

        # hits all values
        fail_value = 0
        error = False
        possible_values = list(range(-test, test + 1))
        for i in range(r):
            outcome, res = run_safe(lambda: bumper.get_random(test))
            if not outcome:
                error = True
                fail_value = res
                break
            try:
                possible_values.remove(res)
            except:
                pass
        if error:
            get_random_section.add_items(Test(f'hits all values test {j}', fail_value, f'between -{test} and {test}'))
        elif len(possible_values) > 0:
            get_random_section.add_items(
                Test(f'hits all values test {j}', f'values not returned from function', f'between -{test} and {test}',
                     data=possible_values))
        else:
            get_random_section.add_items(Test(f'hits all values test {j}', True, True, show_actual_expected=False))

    # HIT VERTICAL TESTS
    hit_vertical_section = Section('hit_vertical()')
    for i, test in enumerate(test_cases.hit_vertical_tests):
        expected = test['expected']
        circle = Circle(Point(test['x'], test['y']), test['radius'])
        width = test['width']
        height = test['height']
        data = [circle, f'width: {width}', f'height: {height}']
        win = MockWin(width, height)
        _, res = run_safe(lambda: bumper.hit_vertical(circle, win))
        hit_vertical_section.add_items(Test(f'test {i}', res, expected, data))

    # HIT HORIZONTAL TESTS
    hit_horizontal_section = Section('hit_horizontal()')
    for i, test in enumerate(test_cases.hit_horizontal_tests):
        expected = test['expected']
        circle = Circle(Point(test['x'], test['y']), test['radius'])
        width = test['width']
        height = test['height']
        data = [circle, f'width: {width}', f'height: {height}']
        win = MockWin(width, height)
        _, res = run_safe(lambda: bumper.hit_horizontal(circle, win))
        hit_horizontal_section.add_items(Test(f'test {i}', res, expected, data))

    section.add_items(collide_section, get_random_section, hit_vertical_section, hit_horizontal_section)
    return section
