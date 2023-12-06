""" collections for python bit operations """

def parity_brute(x: int)->int:
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result


def parity_lowest_set_bit(x: int)->int:
    result = 0
    while x:
        result ^= 1
        x &= x - 1
    return result

def parity(x: int, func_name: str='lowest_set_bit')->int:
    if func_name == 'lowest_set_bit':
        return parity_lowest_set_bit(x)
    elif func_name == 'brute':
        return parity_brute(x)
    else:
        assert 0

