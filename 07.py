'''
Solution for Advent of Code 2020, Day 7.
https://adventofcode.com/2020/day/7
Adam Matan <adam@matan.name>, 2021
'''

import re
import sys
import logging

SHINY_GOLD = 'shiny gold'

def parse_input(filename):
    with open(filename) as f:
        rows = f.readlines()

    reg = re.compile(r'''
        ([a-z][a-z\s]+?)        # Bag name
        \s                      # Space
        bag                     # the word bag (or bags) as a separator
        ''',
        re.VERBOSE)
    bags_map = {}
    for row in rows:
        bags_in_row = reg.findall(row)
        container_bag, contained_bags = bags_in_row[0], bags_in_row[1:]
        if 'contain no other' in contained_bags[0]:
            contained_bags = []
        bags_map[container_bag] = set(contained_bags)
    return bags_map

def has_shiny_gold(container_bag, bags_map):
    '''
    >>> bags_map = {'vibrant plum': {'dull turquoise', 'dark black', 'shiny gold'}, \
                    'bright red': {}, \
                    'light cyan': {'vibrant plum'}}
    >>> has_shiny_gold('vibrant plum', bags_map)
    True
    >>> has_shiny_gold('light cyan', bags_map)
    True
    >>> has_shiny_gold('bright red', bags_map)
    False
    '''
    contained_bags = bags_map[container_bag]
    if SHINY_GOLD in contained_bags:
        return True
    for bag in contained_bags:
        if has_shiny_gold(bag, bags_map):
            return True
    return False


def part_1(filename):
    '''
    >>> part_1('07.txt')
    300
    >>> part_1('07-small.txt')
    4
    '''
    bags_map = parse_input(filename)
    return sum([has_shiny_gold(bag, bags_map) for bag in bags_map])

def part_2(filename):
    '''
    >>> part_2('07.txt')
    True
    '''    
    return True

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else '07.txt'
    logging.basicConfig(level='WARN') # Set to INFO for debugging
    print(part_1(filename))
    print(part_2(filename))

