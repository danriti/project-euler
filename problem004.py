#!/usr/bin/python

def is_palindrome(number):
    return str(number) == str(number)[::-1]

def get_largest_palindrome(min, max):
    largest = 0

    for i in reversed(range(min, max)):
        for j in reversed(range(min, max)):
            product = i * j

            if is_palindrome(product) and largest > biggest:
                largest = product

    return biggest

print get_largest_palindrome(100, 1000)
