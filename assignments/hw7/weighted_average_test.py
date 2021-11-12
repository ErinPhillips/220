import json

from hw7.weighted_average import weighted_average
from tests import api_service
from tests.test_framework import *


class TestClass:

    def test_hw(self):
        builder = TestBuilder('Weighted Average', 'weighted_average.py', 15, 1)
        builder.rc_file = '../../tests/hw5/.pylintrc'
        static_section = build_static_section()
        dynamic_section = build_dynamic_section()
        builder.add_items(static_section, dynamic_section)
        builder.run()


# static tests
def build_static_section():
    file_prefix = 'static_test'
    inputs = [
        [
            "Billy Bother's average: 87.0",
            "Oh No's average: Error: The weights are less than 100.",
            "Hermione Heffalump's average: 95.4",
            "Too Bad's average: Error: The weights are more than 100.",
            "Kurt Kidd's average: 82.5",
            "Class average: 88.3"
        ],
        [
            "James Hook's average: 97.0",
            "Class average: 97.0"
        ],
        [
            "Doll R. Bill's average: 80.0",
            "Frank N. Stein's average: 50.0",
            "Howe D. Pardner's average: 30.3",
            "Mary Thonn's average: Error: The weights are more than 100.",
            "Nadia Seymour's average: 100.0",
            "Phil Down's average: 0.0",
            "Class average: 52.1"
        ]

    ]
    return run_test(inputs, file_prefix, 'static tests')


# dynamic tests
def build_dynamic_section():
    file_prefix = 'api_test'
    response = api_service.test('hw6', 'GET', params={'number': 10})
    answers = json.loads(response.text)
    expected_values = []
    for i, test in enumerate(answers):
        with open(f'../../tests/hw6/{file_prefix}{i}', 'w') as f:
            f.writelines('\n'.join(test['testData']))
        expected_values.append(test['expectedValues'])
    return run_test(expected_values, file_prefix, 'api tests')


def run_test(data, file_prefix, test_type):
    section = Section(test_type)
    for test_number, test in enumerate(data):
        weighted_average(f'../../tests/hw6/{file_prefix}{test_number}',
                         f'../../tests/hw6/{file_prefix}_output{test_number}')
        expected_lines = test
        actual_lines = []
        inputs = open(f'../../tests/hw6/{file_prefix}{test_number}', 'r').read()
        with open(f'../../tests/hw6/{file_prefix}_output{test_number}') as f:
            sub_section = Section(f'test {test_number}', group_data=inputs.split('\n'))
            for index, line in enumerate(f):
                actual_line = line.strip()
                actual_lines.append(actual_line)
                sub_section.add_items(Test(f'test {index}', actual_line, expected_lines[index]))
        section.add_items(sub_section)
    return section
