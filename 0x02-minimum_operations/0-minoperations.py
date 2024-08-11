#!/usr/bin/python3
"""
This module defines the minOperations function that calculates the fewest
number of operations needed to achieve exactly n 'H' characters in a file
using only "Copy All" and "Paste" operations.
"""


def minOperations(n):
    """
    Calculates the minimum number of operations needed to get exactly n 'H'
    characters.

    Parameters:
    n (int): The target number of 'H' characters.

    Returns:
    int: The minimum number of operations required, or 0 if n is impossible
    to achieve.
    """
    if (n < 2):
        return 0
    ops, root = 0, 2
    while root <= n:
        if n % root == 0:
            ops += root
            n = n / root
            root -= 1
        root += 1
    return ops
