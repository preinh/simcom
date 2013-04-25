__author__ = 'pirchiner'

from numpy import array
from gauss import gaussClassic

a = array([ [ 8.,  -6.,  2.], \
            [-4.,  11., -7.], \
            [ 4.,  -7.,  6.] ])

b = array( [28., -40., 33.])

print a, b.flatten(1), gaussClassic.gaussElimin(a, b.flatten(1))
