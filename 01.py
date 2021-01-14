import sys
import logging

def get_input(filename):
    with open(filename) as f:
        expenses = [int(s) for s in f.readlines()]
    return expenses

def part_1(filename):
    '''
    >>> part_1('01.txt')
    955584
    >>> part_1('01-small.txt')
    514579
    '''
    expenses = get_input(filename)
    for i in expenses:
        for j in expenses:
            if i+j == 2020:
                return i*j
    raise ValueError('No match found')

def part_2(filename):
    '''
    >>> part_2('01.txt')
    287503934
    >>> part_2('01-small.txt')
    241861950
    '''    
    expenses = get_input(filename)
    for i in expenses:
        for j in expenses:
            for k in expenses:
                if i+j+k == 2020:
                    return i*j*k
    raise ValueError('No match found')

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else '01.txt'
    logging.basicConfig(level='WARN') # Set to INFO for debugging
    print(part_1(filename))
    print(part_2(filename))