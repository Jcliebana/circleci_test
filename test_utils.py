"""
Unit tests for the utils library
"""

import utils


class TestCalculator:

    def test_addition(self):
        assert 4 == utils.add(2, 2)

    def test_subtraction(self):
        assert 2 == utils.subtract(4, 2)
