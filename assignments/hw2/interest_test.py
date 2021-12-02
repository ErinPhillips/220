from hw2 import interest
from tests.hw2 import random_tests
from tests.test_framework import *


class TestClass:

    def test_stuff(self, monkeypatch, capfd):
        builder = TestBuilder('Interest', 'interest.py', 20, 5)
        static_section = static_tests('Static', monkeypatch, capfd)
        dynamic_section = dynamic_tests('Dynamic', monkeypatch, capfd)
        builder.add_items(static_section, dynamic_section)
        builder.run()


def static_tests(name, monkeypatch, capfd):
    inputs = [
        (['15.84', '31', '850', '400', '20'], '9.35'),
        (['7.07', '30', '700', '100', '1'], '3.55'),
        (['0', '29', '0', '100', '29'], '0.0'),
        (['99', '31', '1234', '1234', '31'], '101.81')
    ]
    return run_test(inputs, name, monkeypatch, capfd)


def dynamic_tests(name, monkeypatch, capfd):
    data = random_tests.create(10)
    input = data['data']
    res = data['res']
    test_data = convert_test_data(input, res)
    return run_test(test_data, name, monkeypatch, capfd)


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


def convert_test_data(data, response):
    inputs = []
    for index, values in enumerate(data):
        input = list(map(str, [values['rate'], values['days'], values['previousBalance'], values['payment'],
                               values['paymentDay']]))
        inputs.append((input, str(response[index])))
    return inputs
