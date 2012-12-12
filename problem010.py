#!/usr/bin/python

import math

TWO_MILLION = 2000000

def is_prime_number(num):
    if num < 0:
        return False
    for i in xrange(2, int(math.sqrt(num))+1):
        if (num % i) == 0:
            return False
    return True

sum_of_primes = 0

for i in xrange(2, TWO_MILLION):
    if is_prime_number(i):
        sum_of_primes += i

print sum_of_primes
