#!/usr/bin/python

def find_pythagorean_triplet():
    for a in xrange(1, 1000):
        for b in xrange(1, 1000):
            for c in xrange(1, 1000):
                if ((a < b) and (b < c)) and \
                   ((a + b + c) == 1000) and \
                   ((a**2 + b**2) == c**2):
                    return [a, b, c]

product = 1
triplet = find_pythagorean_triplet()

for i in triplet:
    product *= i

print product
