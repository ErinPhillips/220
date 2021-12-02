import os

from hw7.weighted_average import weighted_average
from tests.hw7 import random_tests
from tests.test_framework import *


class TestClass:

    def test_hw(self):
        builder = TestBuilder('Weighted Average', 'weighted_average.py', 15, 1)
        builder.rc_file = '../../tests/hw6/.pylintrc'
        static_section, static_files = build_static_section()
        dynamic_section, dynamic_files = build_dynamic_section()
        builder.add_items(static_section, dynamic_section)
        builder.run()
        for input_file, output_file in static_files:
            os.remove(output_file)
        for input_file, output_file in dynamic_files:
            os.remove(input_file)
            os.remove(output_file)


test_folder = '../../tests/hw7'


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
    file_prefix = 'dynamic_test'
    answers = random_tests.create(10)
    expected_values = []
    for i, test in enumerate(answers):
        with open(f'{test_folder}/{file_prefix}{i}', 'w') as f:
            f.writelines('\n'.join(test['testData']))
        expected_values.append(test['expectedValues'])
    return run_test(expected_values, file_prefix, 'dynamic tests')


def run_test(data, file_prefix, test_type):
    section = Section(test_type)
    files = []
    for test_number, test in enumerate(data):
        input_file = f'{test_folder}/{file_prefix}{test_number}'
        output_file = f'{test_folder}/{file_prefix}_output{test_number}'
        files.append((input_file, output_file))
        weighted_average(input_file, output_file)
        expected_lines = test
        actual_lines = []
        inputs = open(f'{test_folder}/{file_prefix}{test_number}', 'r').read()
        with open(f'{test_folder}/{file_prefix}_output{test_number}') as f:
            sub_section = Section(f'test {test_number}', group_data=inputs.split('\n'))
            for index, line in enumerate(f):
                actual_line = line.strip()
                actual_lines.append(actual_line)
                sub_section.add_items(Test(f'test {index}', actual_line, expected_lines[index]))
        section.add_items(sub_section)
    return section, files
