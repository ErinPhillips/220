import json

from hw6 import vigenere
from tests import api_service
from tests.test_framework import *


class TestClass:

    def test_hw(self):
        builder = TestBuilder('Vigenere', 'vigenere.py', 15, 5)
        builder.rc_file = '../../tests/hw5/.pylintrc'
        static_tests = build_static_tests()
        dynamic_tests = build_dynamic_tests()
        builder.add_items(static_tests, dynamic_tests)
        builder.run()


def build_static_tests():
    inputs = [
        (('this program will be great', 'python'), 'IFBZDEDEKHAJXJEISTGCTA'),
        (('the time has come the walrus said', 'oyster'), 'HFWMMDSFSLGFACLAINOJJNWJOGV'),
        (('float like a butterfly', 'champ'), 'HSOMINPKQPDBTFTTMLK')
    ]
    return run_test(inputs, 'static tests')


def build_dynamic_tests():
    response = api_service.test('hw5', 'GET', params={'number': 12})
    answers = json.loads(response.text)
    test_data = convert_test_data(answers)
    return run_test(test_data, 'dynamic tests')


def run_test(data, test_type):
    section = Section(test_type)
    for inp in data:
        message = inp[0][0]
        key = inp[0][1]
        expected = inp[1]
        actual = vigenere.code(message, key)
        section.add_items(Test(message, actual, expected, [f'message: {message}', f'key: {key}']))
    return section


def convert_test_data(data):
    inputs = []
    for test in data:
        inputs.append(((test['message'], test['key']), test['cipherText']))
    return inputs
