#!/usr/bin/python

n = 600851475143
i = 2

while n != i:
    if (n % i) == 0:
        n /= i
        i = 2
    else:
        i += 1

print n
