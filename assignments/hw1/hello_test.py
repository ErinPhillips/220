from hw1 import hello
from tests.test_framework import *


class TestClass:

    def test_input(self, capfd):
        builder = TestBuilder("Hello World!", 'hello.py', linter_points=20, default_test_points=70)

        hello.main()
        captured = capfd.readouterr()
        actual = captured.out.strip()
        expected = "hello, world!"

        test = Test('print hello, world!', actual, expected)
        builder.add_items(test)

        builder.run()
