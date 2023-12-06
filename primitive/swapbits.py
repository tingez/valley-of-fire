""" collections for operation to swap bits"""


def swap_bits(x: int, i: int, j: int)->int:
    """
        swap bits of x at index i and j (0-based)
        parameter error will return zero
    """
    bit_len = x.bit_length()
    if i < 0 or i >= bit_len or j < 0 or j >= bit_len:
        return 0

    if (x >> i) & 0x1 != (x >> j) & 0x1:
        bit_mask = (0x1 << i) | (0x1 << j)
        x ^= bit_mask

    return x


def reverse_bits(x):
    bit_len = x.bit_length()
    mean_idx = bit_len // 2
    for idx in range(mean_idx):
        x = swap_bits(x, idx, bit_len-1-idx)
    return x
