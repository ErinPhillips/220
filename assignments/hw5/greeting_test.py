"""
a lump sum of points are awarded per test.
you cannot lose more points for a test than the max points per test
"""
from tests.test_framework import TestBuilder


class TestClass:

    def test_hw(self):
        builder = TestBuilder('greeting', 'greeting.py', 20, 1)
        builder.add_to_blacklist({
            'importturtle': "turtle graphics is not allowed for this assignment. please use the author's graphics package.",
            'fromturtle': "turtle graphics is not allowed for this assignment. please use the author's graphics package."
        })
        builder.run()
