'''
Solution for Advent of Code 2020, Day 6.
https://adventofcode.com/2020/day/6
Adam Matan <adam@matan.name>, 2021
'''

import sys
import logging

def parse_input(filename):
    with open(filename) as f:
        groups = f.read().split('\n\n')
    return groups

def part_1(filename):
    '''
    >>> part_1('06-small.txt')
    11
    >>> part_1('06.txt')
    7027
    '''
    groups = parse_input(filename)
    declarations = [g.replace('\n', '') for g in groups]
    return sum([len(set(g)) for g in declarations])

def part_2(filename):
    '''
    >>> part_2('06-small.txt')
    6
    >>> part_2('06.txt')
    3579
    '''
    groups = parse_input(filename)
    count = 0
    for group in groups:
        declarations = [set(d) for d in group.strip().split('\n')]
        shared_declaration = declarations[0]
        for declaration in declarations[1:]:
            shared_declaration = shared_declaration.intersection(declaration)
        count += len(shared_declaration)

    return count

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else '06.txt'
    logging.basicConfig(level='INFO') # Set to INFO for debugging
    print(part_1(filename))
    print(part_2(filename))

