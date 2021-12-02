import random

from graphics import GraphWin, Point, Rectangle, Text

from hw9.button import Button
from tests.test_framework import *

win = GraphWin("Three Door Game", 600, 600)


class TestClass:
    def test_hw(self):
        builder = TestBuilder('button', 'button.py', 12)
        builder.add_lint_test('three_door_game.py', 10)
        constructor_section, instance_vars_section, methods_section = build_sections()
        builder.add_items(constructor_section, instance_vars_section, methods_section)
        builder.run()


def build_sections():
    LABEL = "OK"
    rec_point_a = Point(1, 2)
    rec_point_b = Point(3, 4)
    rec = Rectangle(rec_point_a, rec_point_b)

    # Test Constructor
    constructor_section = Section("constructor")
    my_button = None
    try:
        my_button = Button(rec, LABEL)
        constructor_section.add_items(Test('initialize constructor', True, True))
    except Exception as e:
        print('\nFAILED: Could not initialize Button, no more test will run.')
        sys.exit(1)

    # test instance variables
    instance_vars_section = Section('instance variables')
    # shape
    instance_vars_section.add_items(Test("instance variable shape", type(my_button.shape), Rectangle))
    # text
    instance_vars_section.add_items(Test("instance variable text", type(my_button.text), Text))

    # test methods
    methods_section = Section('methods')
    # get_label
    label_test = Test("get_label", my_button.get_label(), LABEL)
    # draw
    outcome, res = run_safe(my_button.draw(win))
    if outcome:
        draw_test_rect = Test('draw rectangle', win.items[0], rec)
        draw_test_text = Test('draw text', win.items[1].getText(), LABEL)
    else:
        draw_test_rect = Test('draw rectangle', win.items[0], rec)
        draw_test_text = Test('draw text', win.items[1].getText(), LABEL)
    # undraw
    my_button.undraw()
    undraw_test = Test('undraw', len(win.items), 0)
    methods_section.add_items(label_test, draw_test_rect, draw_test_text, undraw_test)

    # is_clicked
    is_clicked_values = build_is_clicked_tests(rec_point_a, rec_point_b)
    is_clicked_subsection = Section('is_clicked()')
    for test in is_clicked_values:
        is_clicked = my_button.is_clicked(test[0])
        is_clicked_subsection.add_items(Test('click test', is_clicked, test[1], data=[f'click point: {test[0]}',
                                                                                      f'button dimensions: {(my_button.shape.getP1(), my_button.shape.getP2())}']))
    # color_button
    color_button_subsection = Section('color_button()')
    for color in get_colors():
        my_button.color_button(color)
        color_button_subsection.add_items(Test('color button', my_button.shape.config["fill"], color))

    # set_label
    set_label_subsection = Section('set_label()')
    for label in get_colors():
        my_button.set_label(label)
        set_label_subsection.add_items(Test('set label', my_button.text.getText(), label))

    methods_section.add_items(is_clicked_subsection)
    methods_section.add_items(color_button_subsection)
    methods_section.add_items(set_label_subsection)

    return (constructor_section, instance_vars_section, methods_section)


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
