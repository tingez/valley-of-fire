"""
module about binary reflected Gray code
a minimal-change algorithm for generating bit strings
every one of them differs from its immediate predecessor by only a single bit
leetcode refer to https://leetcode.com/problems/gray-code/description/

"""
from typing import List

def gray_code(n: int)->List[int]:
    """
    ALGORITHM BRGC(n)
        //Generates recursively the binary reflected Gray code of order n
        //Input: A positive integer n
        //Output: A list of all bit strings of length n composing the Gray code
        if n = 1 make list L containing bit strings 0 and 1 in this order
        else generate list L1 of bit strings of size n − 1 by calling BRGC(n − 1)
            copy list L1 to list L2 in reversed order
            add 0 in front of each bit string in list L1
            add 1 in front of each bit string in list L2
            append L2 to L1 to get list L
        return L
    """
    if n == 1: return [0, 1]

    prev_list = gray_code(n-1)
    curr_list = prev_list[:]
    curr_list.reverse()

    for idx in range(n-1):
        curr_list[idx] |= 0x1 << (n-1)

    return prev_list.extend(curr_list)
