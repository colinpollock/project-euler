"""Problem 1 - Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

http://projecteuler.net/problem=1
"""

def sum_multiples(num):
    return sum(n for n in xrange(1, num) if n % 3 == 0 or n % 5 == 0)


if __name__ == '__main__':
    assert sum_multiples(10) == 23
    print sum_multiples(1000)
