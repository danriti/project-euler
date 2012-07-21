#!/usr/bin/python

sumOfSquares = 0
squareOfSums = 0

for i in range(1, 101):
    sumOfSquares += i*i
    squareOfSums += i

print (squareOfSums * squareOfSums) - sumOfSquares
