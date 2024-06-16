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
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
            factor += 1

    return operations
