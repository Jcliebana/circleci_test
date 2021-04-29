"""
Unit tests for the utils library
"""
import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import utils


class TestCalculator:

    def test_addition(self):
        assert 4 == utils.add(2, 2)

    def test_subtraction(self):
        assert 2 == utils.subtract(4, 2)
