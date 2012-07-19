#!/usr/bin/python

max = 4000000
a = 1
b = 0
sum = 0

while a < max:
    a, b = a + b, a

    if (a % 2) == 0:
        sum += a

print "Sum: ", sum
