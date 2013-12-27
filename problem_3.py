"""Problem 3 - Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

http://projecteuler.net/problem=3
"""

from collections import Counter
from operator import itemgetter


def find_prime_factors(n, factors=None):
    if factors is None:
        factors = Counter()

    for fac in xrange(2, n // 2):
        div, mod = divmod(n, fac)

        if mod == 0:
            factors[fac] += 1
            return find_prime_factors(div, factors)

    factors[n] += 1
    return factors


def lpf(n):
    return max(find_prime_factors(n).iteritems(), key=itemgetter(1))[0]


if __name__ == '__main__':
    assert find_prime_factors(12) == Counter([2, 2, 3])
    assert lpf(13195) == 29

    print lpf(600851475143)
