from random import randint


def create(number):
    return {
        'didCollideTests': make_did_collide_tests(number),
        'getRandomTests': make_get_random_tests(number),
        'hitVerticalTests': make_hit_tests(number, make_vertical_test),
        'hitHorizontalTests': make_hit_tests(number, make_horizontal_test)
    }


def make_did_collide_tests(number):
    tests = []
    for i in range(number):
        if i % 2 == 0:
            tests.append((make_false_collide_test(lambda x, y: x > y, True), True))
        else:
            tests.append((make_false_collide_test(lambda x, y: x <= y, False), False))
    return tests


def make_false_collide_test(op, expected):
    x1 = randint(50, 100)
    y1 = randint(50, 100)
    r1 = randint(1, 49)
    r2 = randint(1, 49)
    x2 = randint(0, 100)
    y2 = randint(0, 100)
    while op((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2), (r1 + r2) * (r1 + r2)):
        x2 = randint(0, 100)
        y2 = randint(0, 100)

    return {
        'x1': x1,
        'y1': y1,
        'r1': r1,
        'x2': x2,
        'y2': y2,
        'r2': r2,
        'expected': expected
    }


def make_get_random_tests(number):
    random_numbers = []
    for i in range(number):
        random_numbers.append(randint(1, 100))
    return random_numbers


def make_hit_tests(number, vert_or_horz):
    tests = []

    def add(x, y):
        return x + y

    def sub(x, y):
        return x - y

    res = True
    ops = [sub, add]
    for i in range(number):
        tests.append(vert_or_horz(ops[0], ops[1], res))
        res = not res
        ops = [add, sub]
        if res:
            ops = [sub, add]
    return tests


def make_horizontal_test(op1, op2, expected):
    radius = randint(1, 100)
    width = randint(100, 1000)
    height = randint(radius * 2 + 2, 1000)  # necessary to avoid collisions with other side than what is being tested
    top_side = bool(randint(0, 1))
    x = randint(1, width)
    y = op1(radius, 1) if top_side else op2((height - radius), 1)
    return {
        'radius': radius,
        'x': x,
        'y': y,
        'expected': expected,
        'width': width,
        'height': height
    }


def make_vertical_test(op1, op2, expected):
    radius = randint(1, 100)
    width = randint(radius * 2 + 2, 1000)  # necessary to avoid collisions with other side than what is being tested
    height = randint(100, 1000)
    left_side = bool(randint(0, 1))
    y = randint(1, height)
    x = op1(radius, 1) if left_side else op2((width - radius), 1)
    return {
        'radius': radius,
        'x': x,
        'y': y,
        'expected': expected,
        'width': width,
        'height': height
    }
