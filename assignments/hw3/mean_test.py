import json

from hw3 import mean
from tests import api_service
from tests.test_framework import *


class TestClass:

    def test_hw(self, monkeypatch, capfd):
        outline = TestBuilder('mean', 'mean.py', 12, 2)
        outline.rc_file = '../../tests/hw3/.pylintrc'
        outline.add_to_blacklist({
            'importstatistics': 'statistics library not allowed - please write your program to calculate the averages and do not rely on outside libraries to do so for you.',
            'fromstatistics': 'statistics library not allowed - please write your program to calculate the averages and do not rely on outside libraries to do so for you.'
        })
        static_tests = self.static_test_builder(monkeypatch, capfd)
        api_tests = self.api_test_builder(monkeypatch, capfd)
        outline.add_items(static_tests, api_tests)
        outline.run()
        # static tests

    def static_test_builder(self, monkeypatch, capfd):
        inputs = [
            (['4', '10', '5', '2', '5'], {'rms_average': 6.205, 'harmonic_mean': 4.0, 'geometric_mean': 4.729}),
            (['1', '1'], {'rms_average': 1.0, 'harmonic_mean': 1.0, 'geometric_mean': 1.0}),
            (['10', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
             {'rms_average': 6.205, 'harmonic_mean': 3.414, 'geometric_mean': 4.529}),
            (['5', '5', '5', '5', '5', '5'], {'rms_average': 5.0, 'harmonic_mean': 5.0, 'geometric_mean': 5.0})
        ]
        return self.run_test(inputs, 'static tests', monkeypatch, capfd)

    # dynamic tests
    def api_test_builder(self, monkeypatch, capfd):
        response = api_service.test('hw2', 'GET', params={'number': 9})
        data = json.loads(response.text)
        input = data['data']
        answers = data['answers']
        test_data = self.convert_test_data(input, answers)
        return self.run_test(test_data, 'api tests', monkeypatch, capfd)

    @staticmethod
    def run_test(data, test_type, monkeypatch, capfd):
        outputs = []
        for inp in data:
            userIn = inp[0]
            i = iter(userIn)
            monkeypatch.setattr('builtins.input', lambda inputMessage: next(i))
            mean.main()
            captured = capfd.readouterr()
            output = captured.out.strip().split('\n')
            outputs.append({'rms_average': float(output[0]), 'harmonic_mean': float(output[1]),
                            'geometric_mean': float(output[2]), 'data': userIn})

        section = Section(test_type)
        for index, actual in enumerate(outputs):
            expected = data[index][1]
            test_results = [
                {'name': 'rms_average', 'actual': actual['rms_average'], 'expected': expected['rms_average']},
                {'name': 'harmonic_mean', 'actual': actual['harmonic_mean'],
                 'expected': expected['harmonic_mean']},
                {'name': 'geometric_mean', 'actual': actual['geometric_mean'],
                 'expected': expected['geometric_mean']},
            ]
            sub_section = Section(f'test {index + 1}', group_data=[" ".join(map(str, actual['data']))])
            for i in test_results:
                sub_section.add_items(Test(i['name'], i['actual'], i['expected']))
            section.add_items(sub_section)
        return section

    @staticmethod
    def convert_test_data(data, response):
        inputs = []
        for index, test in enumerate(response):
            input_values = list(map(str, data[index]))
            input_values.insert(0, str(len(data[index])))
            output_values = {
                'rms_average': test['rmsAvg'],
                'harmonic_mean': test['harmonicMean'],
                'geometric_mean': test['geometricMean']
            }
            inputs.append((input_values, output_values))
        return inputs
