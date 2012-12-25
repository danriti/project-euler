#!/usr/bin/python

ONE_MILLION = 1000000

def get_collatz(start):
    lst = []
    i = start
    while True:
        lst.append(i)
        if i == 1:
            break
        elif (i % 2) == 0:
            i /= 2
        else:
            i = (3 * i) + 1
    return lst

def main():
    largest_chain = 0
    start_value = 0
    chain = 0
    for i in range(1, ONE_MILLION):
        chain = get_collatz(i)
    
        if len(chain) > largest_chain:
            start_value = i
            largest_chain = len(chain)

    print start_value, largest_chain

if __name__ == "__main__":
    main()
