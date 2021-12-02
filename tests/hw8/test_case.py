class TestCase:

    def __init__(self):
        self.did_collide_tests = []
        self.get_random_tests = []
        self.hit_vertical_tests = []
        self.hit_horizontal_tests = []


class Result:

    def __init__(self, points):
        self.passed = False
        self.actual = None
        self.expected = None
        self.data = None
        self.points = points


class Results:
    """
    None points indicates that the points will just be those added from the individual tests
    If points is given, that will be the maximum points gained/lost, regardless of how many
    individual tests are done
    """

    def __init__(self, points):
        self.points = points
        self.number_passed = 0
        self.number_failed = 0
        self.total_points = 0
        self.failed_tests = []

    def get_total_points(self):
        if self.points and self.total_points > self.points:
            return self.points
        return self.total_points

    def add(self, res: Result):
        if res.passed:
            self.number_passed += 1
            self.total_points += res.points
        else:
            self.number_failed += 1
            self.failed_tests.append(res)
