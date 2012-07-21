#!/usr/bin/python

import math

def is_prime_number(num):
    if num <0:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if (num % i) == 0:
            return False
    return True

i = 1
c = 0
p = 0

while c < 10001:
    if is_prime_number(i):
        c += 1
        p = i
    i += 1

print c, p
