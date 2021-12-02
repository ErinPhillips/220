import sys
from collections.abc import Callable
from types import LambdaType

from pylint import epylint as lint


class TestItem:
    def __init__(self, name: str, default_points: int):
        # default points are how much an individual test is worth
        #   this is so a section can have a default for all of the questions in the section
        # total points are the sum of the total possible points.
        self.default_points = default_points
        self.total_points = 0
        self.earned_points = 0
        self.name = name
        self.level = 1

    def run(self):
        pass


class Test(TestItem):
    def __init__(self, name, actual=None, expected=None, data=None, points=None, fail_fast=False,
                 show_actual_expected=True):
        """
        A Test in a Test Suite.

        :param name: the name of the test
        :param actual: the value being checked. can be a value or a lambda function
        :param expected: the correct value
        :param data: the data used to generate the test
        :param points: the amount of points the test is worth
        :param fail_fast: exit the test suit if the test fails
        :param show_actual_expected: show the actual and expected values if a test fails
        """
        super().__init__(name, points)
        self.actual = actual
        self.expected = expected
        self.data = data
        self.fail_fast = fail_fast
        self.show_actual_expected = show_actual_expected

    def passed(self):
        self.earned_points += self.default_points
        self.total_points += self.default_points
        tabs = '\t' * self.level
        print(f"{tabs}PASSED: +{self.total_points} - {self.name}")

    def failed(self, result, e=None):
        """
        e is an exception. this would happen when running tests on functions.
        if an exception occurs, we do not show the actual and expected values
        """
        self.total_points += self.default_points
        tabs = '\t' * self.level
        print(f'{tabs}FAILED: -{self.default_points}: {self.name}')
        if self.fail_fast:
            sys.exit()
        if self.show_actual_expected and not e:
            print(f'{tabs}\tactual: {result} | expected: {self.expected}')
        if self.data:
            print(f'{tabs}\tdata:')
            for line in self.data:
                print(f'{tabs}\t\t{line}')
        if e:
            print(f'{tabs}\tan exception was thrown while running this test:')
            print(f'{tabs}\t\t{e}:')

    def run(self, level=1):
        self.level = level
        try:
            result = self.actual
            if isinstance(self.actual, LambdaType):
                result = self.actual()
            if result == self.expected:
                self.passed()
            else:
                self.failed(result)
        except Exception as e:
            self.failed(e)

    def fail_fast(self):
        self.fail_fast = True
        return self


class Section(TestItem):
    def __init__(self, name, points=None, custom_total_points=None, group_data=None):
        """
        A section of a Test Suite. Can be made up of other sections and/or individual :class:`Test <tests.test_framework.TestItem>`

        :param name: the name of the section
        :param points: the default number of points to be awarded for each item in the section
        :param custom_total_points: if set, these points are awarded up front and points are subtracted for wrong answers
        :param group_data: if set, data will be displayed for the entire section if a test fails rather than individual tests
        """
        super().__init__(name, points)
        self.outline: list[TestItem] = []
        self.custom_total_points = custom_total_points
        # case where points are assigned up front and subtracted for wrong answers
        if not custom_total_points is None:
            self.total_points = custom_total_points
            self.earned_points = custom_total_points
        # used to indicate if one set of test data should be used for all the tests
        self.group_data = group_data

    def add_items(self, *items: TestItem):
        for item in items:
            self.outline.append(item)

    def run(self, level=1):
        tabs = '\t' * level
        start_label = f' {self.name} start '
        print()
        print('{0}{1:-^70}'.format(tabs, start_label))
        for item in self.outline:
            if item.default_points is None:
                item.default_points = self.default_points
            item.run(level + 1)
            if self.custom_total_points is None:
                self.total_points += item.total_points
                self.earned_points += item.earned_points
            # case where points are assigned up front and subtracted for wrong answers
            else:
                self.earned_points -= item.total_points
        if self.group_data and self.earned_points < self.total_points:
            print(f'{tabs}\tdata:')
            for line in self.group_data:
                print(f'{tabs}\t\t{line}')
        end_label = f' {self.name} end {self.earned_points}/{self.total_points} '
        print('{0}{1:-^70}'.format(tabs, end_label))


class TestBuilder:
    """
    A TestBuilder

    Attributes
         blacklist:    dict of code that should not be used and the message to display if found
         rc_file:   the file to use for linting tests
         blacklist_func: the function that runs for blacklist tests. takes a tuple parameter with the blacklist and the file_name
                         this can be overridden so no blacklist tests run by setting this to lambda x : None
        lint_func:  the function that runs for linting tests. takes a tuple parameter with the file_name, linter_points, and rc_file
                    this can be overridden so no linting tests run by setting this to lambda x : None


    """

    def __init__(self, name, file_name, linter_points, default_test_points=1):
        """
        The builder of a test suite. Can be made up of sections and/or individual tests`

        :param name: the name of the test
        :param file_name: the name of the file being tested
        :param linter_points: the number of points assigned to linting tests
        :param default_test_points: the default number of points to be awarded for each TestItem in the test suite
        """
        self.outline: list[TestItem] = []
        self.total_points = 0
        self.earned_points = 0
        self.default_test_points = default_test_points
        self.name = name
        self.blacklist = {
            'importos': 'no need for the os module. please remove it to continue.',
            'fromos': 'no need for the os module. please remove it to continue.',
            'importpathlib': 'no need for the pathlib module. please remove it to continue.',
            'frompathlib': 'no need for the pathlib module. please remove it to continue.',
        }
        self.file_name = file_name
        self.rc_file = '../../.pylintrc'
        self.linter_points = linter_points
        self.blacklist_func = create_blacklist_test()
        self.lint_func = create_lint_test()
        self.lint_tests = []

    def create_blacklist_tests(self):
        pass

    def add_to_blacklist(self, items: dict):
        """
        adds the items in the dictionary to the existing blacklist
        """
        self.blacklist.update(items)

    def add_items(self, *items: TestItem):
        for item in items:
            self.outline.append(item)
        return self

    def add_lint_test(self, file_name, points=None, rc_file=None):
        if points is None: points = self.linter_points
        if rc_file is None: rc_file = self.rc_file
        self.lint_tests.append(self.lint_func((file_name, points, rc_file)))

    def run(self, level=0):
        tabs = '\t' * level
        print()
        print()

        ### BLACKLIST TESTS ###
        self.blacklist_func((self.blacklist, self.file_name))
        #######

        ### LINTING TESTS ###
        lint_test = self.lint_func((self.file_name, self.linter_points, self.rc_file))
        if lint_test:
            self.outline.append(lint_test)
        for test in self.lint_tests:
            self.outline.append(test)
        #######

        test_intro = f' Starting test {self.name} '
        print('{0}{1:=^80}'.format(tabs, test_intro))
        print()
        for item in self.outline:
            if item.default_points is None:
                item.default_points = self.default_test_points
            item.run(level=level + 1)
            self.total_points += item.total_points
            self.earned_points += item.earned_points
        print()
        test_outro = f' Test {self.name} complete: {self.earned_points}/{self.total_points} '
        print('{0}{1:=^80}'.format(tabs, test_outro))


class TestSuit:
    """
    A TestSuit
    """

    def __init__(self, name):
        """
        The test suite. Made up of test builders`
        :param name: the name of the test

        """
        self.outline: list[TestBuilder] = []
        self.total_points = 0
        self.earned_points = 0
        self.name = name

    def add_test_builders(self, *items: TestBuilder):
        for item in items:
            self.outline.append(item)
        return self

    def run(self):
        print()
        print()

        test_intro = f' Starting tests {self.name} '
        print('{0:=^80}'.format(test_intro))
        print()
        for item in self.outline:
            item.run(level=1)
            self.total_points += item.total_points
            self.earned_points += item.earned_points
        print()
        test_outro = f' Test {self.name} complete: {self.earned_points}/{self.total_points} '
        print('{0:=^80}'.format(test_outro))


def run_safe(test):
    """
    helper function to try running a function
    test should be a lambda so it gets executed lazily in this try/catch
    returns a tuple (boolean outcome, any result)
    """
    try:
        outcome_result = (True, test())
    except Exception as e:
        outcome_result = (False, e)
    return outcome_result


def create_lint_test():
    def create_lint_section(x) -> Section:
        test_file, points, rc_file = x
        linting = Section(f'Linting {test_file}', custom_total_points=points)
        (pylint_stdout, pylint_stderr) = lint.py_run(f'{test_file} --rcfile {rc_file}', return_std=True)
        output = pylint_stdout.getvalue()
        error_list = output.split("\n")[1:-1]
        # case when the errors exceeds the possible points
        error_range = range(len(error_list))
        if points < len(error_list):
            error_range = range(points)
        for i in error_range:
            linting.add_items(Test(error_list[i], None, 1, points=1, show_actual_expected=False))
        if points < len(error_list):
            linting.add_items(
                Test(f'...and {len(error_list) - points} more errors', None, 1, points=0, show_actual_expected=False))
        return linting

    return create_lint_section


def create_blacklist_test():
    def create_blacklist_code_analyzer(x) -> list[Test]:
        blacklist, test_file = x
        tests = []
        with open(test_file, 'r') as file:
            for index, line in enumerate(file):
                found_items = list(
                    filter(lambda blacklist_key: blacklist_key in line.replace(' ', '').lower(), blacklist.keys()))
                for item in found_items:
                    tests.append(
                        Test(f'Line {index + 1} - {blacklist[item]}', 0, 1, show_actual_expected=False, points=100))
            try:
                tests[-1].fail_fast = True
            except IndexError:
                pass
        for item in tests:
            item.run()

    return create_blacklist_code_analyzer
