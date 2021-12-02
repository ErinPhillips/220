from hw6 import vigenere
from tests.hw6 import random_tests
from tests.test_framework import *


class TestClass:

    def test_hw(self):
        builder = TestBuilder('Vigenere', 'vigenere.py', 15, 5)
        builder.rc_file = '../../tests/hw6/.pylintrc'
        builder.add_to_blacklist({
            'enumerate': 'enumerate() function should not be used in this assignment.'
        })
        static_tests = build_static_tests()
        dynamic_tests = build_dynamic_tests()
        builder.add_items(static_tests, dynamic_tests)
        builder.run()


def build_static_tests():
    inputs = [
        ('this program will be great', 'python', 'IFBZDEDEKHAJXJEISTGCTA'),
        ('the time has come the walrus said', 'oyster', 'HFWMMDSFSLGFACLAINOJJNWJOGV'),
        ('float like a butterfly', 'champ', 'HSOMINPKQPDBTFTTMLK')
    ]
    return run_test(inputs, 'static tests')


def build_dynamic_tests():
    answers = random_tests.create(12)
    test_data = convert_test_data(answers)
    return run_test(test_data, 'dynamic tests')


def run_test(data, test_type):
    section = Section(test_type)
    for inp in data:
        message = inp[0]
        key = inp[1]
        expected = inp[2]
        _, result = run_safe(lambda: vigenere.code(message, key))
        section.add_items(Test(message, result, expected, [f'message: {message}', f'key: {key}']))
    return section


def convert_test_data(data):
    inputs = []
    for test in data:
        inputs.append((test['message'], test['key'], test['cipherText']))
    return inputs
