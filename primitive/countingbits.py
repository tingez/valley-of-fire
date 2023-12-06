"""
    counting bits in an array of integer
    leetcode ref: https://leetcode.com/problems/counting-bits/description/
"""
from typing import List

def count_bits_brute(n: int)->List[int]:
    rst = [0]

    for idx in range(1, n+1):
        bit_length = idx.bit_length()
        tmp_rst = 0
        while bit_length > 0:
            if idx & (0x1 << (bit_length-1)):
                tmp_rst += 1
            bit_length -= 1
        rst.append(tmp_rst)

    return rst
