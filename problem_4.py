"""Problem 4 - Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.

http://projecteuler.net/problem=4
"""
from operator import itemgetter

def is_palindrome(n):
    as_str = str(n)
    return as_str == as_str[::-1]

def multiples(digits):
    for m in xrange(1, 10 ** digits):
        for n in xrange(1, 10 ** digits):

            # Only look at the lower triangle.
            if m >= n:
                product = m * n
                if is_palindrome(product):
                    yield product

def largest_palindrome(digits):
    return max(multiples(digits))

if __name__ == '__main__':
    assert largest_palindrome(2) == 9009
    print largest_palindrome(3)
