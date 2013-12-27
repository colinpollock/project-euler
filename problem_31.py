# coding=utf-8

"""Problem 31 - Coin sums

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?

http://projecteuler.net/problem=31
"""

from util import memoized

@memoized
def make_amount(amount, coins):
    ways = 0

    for idx, coin in enumerate(coins):
        remaining = amount - coin

        if remaining == 0:
            ways += 1

        elif remaining > 0:
            ways += make_amount(remaining, coins[idx:])

    return ways



if __name__ == '__main__':
    coins = (200, 100, 50, 20, 10, 5, 2, 1)
    data = [
        # (1)
        (1, 1),

        # (2), (1, 1)
        (2, 2),

        # (5), (2, 2, 1), (2, 1, 1, 1), (1, 1, 1, 1)
        (5, 4)
    ]

    for amount, expected_num_ways in data:
        found = make_amount(amount, coins)
        reason = 'ways(%d) was %d but expected %d' %  \
                 (amount, found, expected_num_ways)

        assert found == expected_num_ways, reason

    print make_amount(200, coins)
