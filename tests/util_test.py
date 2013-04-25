"""
Tests for the :mod:`myproject.utils` module.
"""

import unittest

from gauss import utils

class AddTestCase(unittest.TestCase):
    """
    Test for the :func:`myproject.utils.add` function.
    """

    def test_add_1_plus_1(self):
        # test adding 1 and 1
        result = utils.add(1, 1)
        self.assertEqual(2, result)

    def test_add_7_plus_5(self):
        # test adding 7 and 5
        result = utils.add(7, 5)
        self.assertEqual(12, result)

    def test_add_neg_12_plus_6pt0(self):
        # test adding -12 and 6.0
        result = utils.add(-12, 6.0)
        self.assertEqual(-6.0, result)
