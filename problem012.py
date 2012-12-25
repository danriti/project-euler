#!/usr/bin/python

import math

def get_divisors(n):    
    factors = []
    factors.append(1)
    # loop to square root as any higher factors can be determined from lower factors
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            factors.append(i) # factor
            factors.append(n/i) # find it's partner
    factors.append(n)
    return set(factors) # sorted unique terms

def main():
    i = 0
    n = 0
    factors = []
    
    while len(factors) < 500:
        i += 1
        n += i
        factors = get_divisors(n)
    
    print n # prints 76576500 

if __name__ == "__main__":
    main()
