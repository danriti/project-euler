""" problem020.py

"""

def factorial(n):
    if n == 1:
        return n
    return n * factorial(n-1)


def main():
    total = 0
    x = factorial(100)

    for i in str(x):
        total += int(i)

    print total


if __name__ == '__main__':
    main()
