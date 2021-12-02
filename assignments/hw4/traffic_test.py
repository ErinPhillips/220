from hw4 import traffic
from tests.hw4 import random_tests
from tests.hw4.test_case import TestCase, Road
from tests.test_framework import *


def input_map(sentence):
    try:
        return float(sentence.split(':')[1].strip())
    except:
        print('\n********************************************************')
        print('could not finish running test. make sure your output has a colon ":" before the value')
        print('********************************************************')
        exit(1)


class TestClass:

    def test_hw(self, monkeypatch, capfd):
        builder = TestBuilder('traffic', 'traffic.py', 10, 1)
        static_tests = build_static_test_section(monkeypatch, capfd)
        dynamic_tests = build_dynamic_test_section(monkeypatch, capfd)
        builder.add_items(static_tests, dynamic_tests)
        builder.run()


def build_static_test_section(monkeypatch, capfd):
    road11 = Road(1, [20, 30, 15, 45])
    road12 = Road(2, [40, 30, 50])
    road13 = Road(3, [30, 60, 15, 55, 20])
    test1 = TestCase([road11, road12, road13])
    road21 = Road(1, [1])
    test2 = TestCase([road21])

    inputs = [test1, test2]
    return run_test(inputs, 'static tests', monkeypatch, capfd)


# dynamic tests
def build_dynamic_test_section(monkeypatch, capfd):
    data = random_tests.create(7, 55)
    return run_test(data, 'dynamic tests', monkeypatch, capfd)


def run_test(test_cases: list[TestCase], test_type, monkeypatch, capfd):
    # get all of the outputs for each test [[test 1 outputs], [test 2 outputs], ...]
    for test_case in test_cases:
        user_in = test_case.get_user_input()
        i = iter(user_in)
        monkeypatch.setattr('builtins.input', lambda input_message: next(i))
        traffic.main()
        captured = capfd.readouterr()
        output = captured.out.strip().split('\n')
        test_case.set_actual_values(list(map(input_map, output)))

    section = Section(test_type)
    for index, test_case in enumerate(test_cases):
        sub_section = Section(f'test {index + 1}', group_data=[f'user inputs: {test_case.get_user_input()}'])

        sub_section.add_items(
            Test('Total Cars', test_case.actual_total_cars, test_case.expected_total_cars),
            Test('Average Cars', test_case.actual_avg_cars, test_case.expected_avg_cars)
        )
        for road_index, road in enumerate(test_case.roads):
            sub_section.add_items(Test(f'Roads {road_index + 1}', road.actual_output, road.expected_output))
        section.add_items(sub_section)
    return section
