# Template for AOC 2020 solutions in Python.
# Remember to change 'template.txt' to the right day number, e.g. '11.txt'

import sys
import logging

def part_1(filename):
    '''
    >>> part_1('template.txt')
    True
    '''
    return True

def part_2(filename):
    '''
    >>> part_2('template.txt')
    True
    '''    
    return True

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else 'template.txt'
    logging.basicConfig(level='WARN') # Set to INFO for debugging
    print(part_1(filename))
    print(part_2(filename))

