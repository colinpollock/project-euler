"""Problem 6 - Sum square difference

The sum of the squares of the first ten natural numbers is:
    12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is:
    (1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.

http://projecteuler.net/problem=6
"""

def sum_of_squares(num):
    return sum(n ** 2 for n in xrange(1, num + 1))

def square_of_sum(num):
    return sum(xrange(num + 1)) ** 2

def sum_square_difference(num):
    return square_of_sum(num) - sum_of_squares(num)


if __name__ == '__main__':
    assert sum_square_difference(10) == 2640
    print sum_square_difference(100)

