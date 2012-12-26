#!/usr/bin/python

ONES = {0 : 'zero',
        1 : 'one',
        2 : 'two',
        3 : 'three',
        4 : 'four',
        5 : 'five',
        6 : 'six',
        7 : 'seven',
        8 : 'eight',
        9 : 'nine'}

TEENS = {10 : 'ten',
         11 : 'eleven',
         12 : 'twelve',
         13 : 'thirteen',
         14 : 'fourteen',
         15 : 'fifteen',
         16 : 'sixteen',
         17 : 'seventeen',
         18 : 'eighteen',
         19 : 'nineteen'}

TENS = {2 : 'twenty',
        3 : 'thirty',
        4 : 'forty',
        5 : 'fifty',
        6 : 'sixty',
        7 : 'seventy',
        8 : 'eighty',
        9 : 'ninety'}

def get_number_letters(n):
    if n == 1000:
        return 'onethousand'

    # Mathematically calculate hundreds (h), tens (t), and ones (o) digits.
    h = n / 100
    t = (n % 100) / 10
    o = n % 10
  
    words = ''
  
    if h > 0:
        words += ONES[h] + 'hundred'

        # Case when handling non rounded hundreds (i.e. 201, not 200)
        if t > 0 or o > 0:
            words += 'and'

    # Case when handling teens (i.e. 12, 115, 417, etc)
    if t == 1:
        words += TEENS[10 + o]
        return words

    if t >= 2:
        words += TENS[t]

        # Case when one's digit is 0 (i.e. 20, 30, 40, 50, etc)
        if o == 0:
            return words

    if o > 0:
        words += ONES[o]

    return words
        
def test_values():
    print 5, get_number_letters(5)
    print 16, get_number_letters(16)
    print 20, get_number_letters(20)
    print 38, get_number_letters(38)
    print 99, get_number_letters(99)
    print 200, get_number_letters(200)
    print 201, get_number_letters(201)
    print 210, get_number_letters(210)
    print 320, get_number_letters(320)
    print 421, get_number_letters(421)
    print 1000, get_number_letters(1000)
    print 342, get_number_letters(342), len(get_number_letters(342))
    print 115, get_number_letters(115), len(get_number_letters(115))

def test_values_range():
    for i in xrange(1, 201):
        print i, get_number_letters(i)

def main():
    letters = 0
    for i in xrange(1, 1001):
        letters += len(get_number_letters(i))
    print letters
        
if __name__ == "__main__":
    #test_values()
    #test_values_range()
    main()
