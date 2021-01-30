'''
Search and replace '12' to adapt.

Solution for Advent of Code 2020, Day 12.
https://adventofcode.com/2020/day/12
Adam Matan <adam@matan.name>, 2021
'''

import sys
import logging

def parse_input(filename):
    '''
    >>> parse_input('12-small.txt')
    [('F', 10), ('N', 3), ('F', 7), ('R', 90), ('F', 11)]
    '''
    with open(filename) as f:
        lines = f.readlines()
    instructions = [(l[0], int(l[1:])) for l in lines]
    return instructions

def part_1(filename):
    '''
    #>>> part_1('12.txt')
    #True
    '''
    directions = {
        'N': [0, 1],
        'S': [0, -1],
        'E': [1, 0],
        'W': [-1, 0]
    }
    rotations = {
        'R': {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'},
        'L': {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
    }

    instructions = parse_input(filename)
    ship_direction = 'E'
    location = [0, 0]
    for instruction in instructions:
        logging.warning('Ship at %s', location)
        orientation, size = instruction
        if orientation in ('R', 'L'):
            while size > 0:
                ship_direction = rotations[orientation][ship_direction]
                size -= 90
            logging.warning('New direction is %s', ship_direction)
        
        if orientation in directions:
            move = [n*size for n in directions[orientation]]
            location = list(map(sum, zip(location, move)))
            logging.warning('Move is %s', move)

        logging.warning(instruction)
    return True

def part_2(filename):
    '''
    >>> part_2('12.txt')
    True
    '''
    _ = parse_input(filename)
    return True

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else '12-small.txt'
    logging.basicConfig(level='WARN') # Set to INFO for debugging
    print(part_1(filename))
    print(part_2(filename))

