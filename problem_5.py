"""Problem 5 - Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

http://projecteuler.net/problem=5
"""

import itertools
import sys


def divides_all(num, max_num):
    return all(num % div == 0 for div in xrange(2, max_num + 1))

def smallest_multiple(max_num):
    # Increment the value by the max number each time since we know the number
    # we're looking for will be a multiple of the max.
    for num in itertools.count(max_num, max_num):
        if divides_all(num, max_num):
            return num


if __name__ == '__main__':
    test_data = [
        (2, 2),
        (3, 6),
        (4, 12),
        (5, 60),
        (6, 60),
        (7, 420),
        (8, 840),
        (9, 2520),
        (10, 2520),
    ]

    for max_num, expected in test_data:
        found = smallest_multiple(max_num)
        assert found == expected

    print smallest_multiple(20)
