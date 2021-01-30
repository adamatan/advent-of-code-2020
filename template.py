'''
Search and replace 'template' to adapt.

Solution for Advent of Code 2020, Day template.
https://adventofcode.com/2020/day/template
Adam Matan <adam@matan.name>, 2021
'''

import sys
import logging

def parse_input(filename):
    '''
    >>> 'blah' in parse_input('template.txt')
    True
    '''
    with open(filename) as f:
        return f.read()

def part_1(filename):
    '''
    >>> part_1('template.txt')
    True
    '''
    _ = parse_input(filename)
    return True

def part_2(filename):
    '''
    >>> part_2('template.txt')
    True
    '''
    _ = parse_input(filename)
    return True

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else 'template.txt'
    logging.basicConfig(level='WARN') # Set to INFO for debugging
    print(part_1(filename))
    print(part_2(filename))

