""" problem021.py

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n). If d(a) = b and d(b) = a, where a != b, then a and
b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""


def main():
    proper_divisors = {1: 1}
    amicable_numbers = []

    # calculate proper divisors
    for i in xrange(2, 10001):
        _sum = 0
        for j in xrange(1, (i/2)+1):
            if i % j == 0:
                _sum += j

        proper_divisors[i] = _sum

    # find amicable pairs
    for a in proper_divisors.keys():
        b = proper_divisors[a]

        if b in proper_divisors and a != b and proper_divisors[a] == b and \
           proper_divisors[b] == a:
            amicable_numbers += [a, b]

    print sum(set(amicable_numbers))


if __name__ == '__main__':
    main()
