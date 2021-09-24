from tests.code_style import code_style
from pylint import epylint as lint


class Test_Framework:
    def __init__(self, global_points=5, sub_points=2, code_style_points=15):
        self.global_points = global_points
        self.sub_points = sub_points
        self.code_style_points = code_style_points
        self.test_total_score = 0
        self.test_total_possible_score = 0
        self.test_questions_correct = 0
        self.test_questions_total = 0
        self.area_score = 0
        self.area_questions_correct = 0
        self.area_questions_total = 0
        self.section_score = 0
        self.section_questions_correct = 0
        self.section_questions_total = 0


    def PASSED(self, test_name):
        self.section_questions_correct += 1
        self.section_score += self.sub_points

        print(f"\tPASSED: +{self.sub_points} - {test_name}")


    def FAILED(self, actual, expected, test_name, data):
        print(f'\tFAILED -{self.sub_points}: {test_name}')
        print(f'\t\tactual: {actual} | expected: {expected}')
        print(f'\t\tdata: {data}')


    def run_test(self, actual, expected, test_name="", data=""):
        self.section_questions_total += 1
        self.test_total_possible_score += self.sub_points

        if actual == expected:
            self.PASSED(test_name)
        else:
            self.FAILED(actual, expected, test_name, data)

    def area_start(self, name):
        self.area_score = 0
        self.area_questions_correct = 0
        self.area_questions_total = 0
        print(f'\n\n============================== {name} start ===============================\n')

    def area_end(self, name):
        self.test_total_score += self.area_score
        self.test_questions_correct += self.area_questions_correct
        self.test_questions_total += self.area_questions_total

        print(f'\n============================== {name} end - {self.area_questions_correct}/{self.area_questions_total} +{self.area_score} ===============================\n')

    def section(self, name):
        self.section_score = 0
        self.section_questions_correct = 0
        self.section_questions_total = 0
        print(f'{name}')

    def section_end(self):
        self.area_score += self.section_score
        self.area_questions_correct += self.section_questions_correct
        self.area_questions_total += self.section_questions_total
        print(f'\t{self.section_questions_correct}/{self.section_questions_total} +{self.section_score}')

    def end_test(self, total_possible):
        total = self.test_total_possible_score if total_possible is None else total_possible
        print(f'\nDONE: {self.test_total_score}/{total}')

    def lint(self, filename, points, rcfile='../../.pylintrc'):
        self.area_questions_total = points
        (pylint_stdout, pylint_stderr) = lint.py_run(f'{filename} --rcfile {rcfile}', return_std=True)
        output = pylint_stdout.getvalue()
        points_off = len(output.split("\n")) - 2
        points_off = 0 if points_off < 0 else points_off

        self.area_questions_correct = 0 if points_off > points else points - points_off
        self.area_score = self.area_questions_correct
        self.test_total_possible_score += points

        passed = points_off <= 0
        if passed:
            print("\nPASSED", f"+{points}")
        else:
            print("\nFAILED")
            print(output)
            print('-' + str(points_off))

