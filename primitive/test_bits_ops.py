""" test code for python bit operations """

from bits_ops import parity


def test_parity():
    assert parity(0b1110100) == 0

