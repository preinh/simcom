"""
Tests for the :mod:`myproject.utils` module.
"""

import unittest

from gauss import gaussClassic
from numpy import array

class AddTestCase(unittest.TestCase):
    """
    Test for the :func:`myproject.utils.add` function.
    """

    def test_solving_simple(self):
        a = array([ [ 8.,  -6.,  2.], \
                    [-4.,  11., -7.], \
                    [ 4.,  -7.,  6.] ])
        b = array(  [28., -40., 33.])

        # test adding 1 and 1
        result = gaussClassic.add(a, b)
        self.assertEqual(array([2, -1, 3]), result)

    # def test_add_7_plus_5(self):
    #     # test adding 7 and 5
    #     result = utils.add(7, 5)
    #     self.assertEqual(12, result)
    #
    # def test_add_neg_12_plus_6pt0(self):
    #     # test adding -12 and 6.0
    #     result = utils.add(-12, 6.0)
    #     self.assertEqual(-6.0, result)
