#!/usr/bin/python

def is_evenly_divisible(min, max, num):
    i = max - 1
    while i > min:
        if (num % i) != 0:
            return False
        i -= 1
    return True

num = 20
while not is_evenly_divisible(2, 20, num):
    num += 20

print num
