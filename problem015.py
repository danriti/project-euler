#!/usr/bin/python

GRID_SIZE = 21

# Ludicrously slow method!
def traverse_grid(path, x, y, count):
    path.append((x, y))
    # End of the grid!
    if x == GRID_SIZE - 1 and \
       y == GRID_SIZE - 1:
        #print path
        return count + 1
    else:
        # You can move right. Do it!
        if (x + 1) <= (GRID_SIZE - 1):
            count = traverse_grid(path, x + 1, y, count)
        # You can move down. Do it!
        if (y + 1) <= (GRID_SIZE - 1):
            count = traverse_grid(path, x, y + 1, count)
    return count
        
#print traverse_grid([], 0, 0, 0)

# Super fast method!
# The number of lattice paths from the origin (0, 0) to a point (a, b) is the 
# binomial coefficient: (a + b / a )
# http://mathworld.wolfram.com/BinomialCoefficient.html

def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1

n = 40
k = 20

print factorial(n) / (factorial(n - k) * factorial(k))
