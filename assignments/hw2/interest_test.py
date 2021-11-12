import json

from tests.test_framework import *

from hw2 import interest
from tests import api_service


class TestClass:

    def test_stuff(self, monkeypatch, capfd):
        builder = TestBuilder('Interest', 'interest.py', 20, 5)
        static_section = TestClass.static_tests('Static', monkeypatch, capfd)
        api_section = TestClass.api_tests('Dynamic', monkeypatch, capfd)
        builder.add_items(static_section, api_section)
        builder.run()

    @staticmethod
    def static_tests(name, monkeypatch, capfd):
        inputs = [
            (['15.84', '31', '850', '400', '20'], '9.35'),
            (['7.07', '30', '700', '100', '1'], '3.55'),
            (['0', '29', '0', '100', '29'], '0.0'),
            (['99', '31', '1234', '1234', '31'], '101.81')
        ]
        return TestClass.run_test(inputs, name, monkeypatch, capfd)

    @staticmethod
    def api_tests(name, monkeypatch, capfd):
        response = api_service.test('hw1', 'GET', params={'number': 10})
        data = json.loads(response.text)
        input = data['data']
        answers = data['answers']
        test_data = TestClass.convert_test_data(input, answers)
        return TestClass.run_test(test_data, name, monkeypatch, capfd)

    @staticmethod
    def run_test(data, name, monkeypatch, capfd) -> Section:
        section = Section(name)
        outputs = []
        for inp in data:
            userIn = inp[0]
            i = iter(userIn)
            monkeypatch.setattr('builtins.input', lambda inputMessage: next(i))
            interest.main()
            captured = capfd.readouterr()
            outputs.append(captured.out.strip())

        for index, actual in enumerate(outputs):
            expected = data[index][1]
            used_data = [f'rate: {float(data[index][0][0])}',
                         f'days: {float(data[index][0][1])}',
                         f'previous_balance: {float(data[index][0][2])}',
                         f'payment: {float(data[index][0][3])}',
                         f'payment_day: {float(data[index][0][4])}'
                         ]
            section.add_items(Test(f'test {index}', actual, expected, used_data))

        return section

    @staticmethod
    def convert_test_data(data, response):
        inputs = []
        for index, values in enumerate(data):
            input = list(map(str, [values['rate'], values['days'], values['previousBalance'], values['payment'],
                                   values['paymentDay']]))
            inputs.append((input, str(response[index])))
        return inputs
