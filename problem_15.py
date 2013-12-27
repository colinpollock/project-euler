"""Problem 15 - Lattice paths

Starting in the top left corner of a 2x2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?

http://projecteuler.net/problem=15
"""

from util import memoized



@memoized
def paths_rec(m, n, height, width):
    if m == height and n == width:
        return 1

    elif m == height:
        return paths_rec(m, n + 1, height, width)

    elif n == width:
        return paths_rec(m + 1, n, height, width)

    else:
        return (paths_rec(m + 1, n, height, width) + 
                paths_rec(m, n + 1, height, width))

def paths(height, width):
    # An N by N grid is actually N+1 by N+1 nodes so we add one each.
    return paths_rec(1, 1, height + 1, width + 1)

if __name__ == '__main__':
    assert paths(2, 2) == 6
    print paths(20, 20)

