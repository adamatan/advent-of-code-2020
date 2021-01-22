'''
Solution for Advent of Code 2020, Day 10.
https://adventofcode.com/2020/day/10
Adam Matan <adam@matan.name>, 2021
'''

import sys
import logging
from collections import Counter

def parse_input(input_filename):
    with open(input_filename) as f:
        lines = f.readlines()
    joltages = [int(line) for line in lines]
    return joltages

def part_1(filename):
    '''
    >>> part_1('10-small.txt')
    35
    >>> part_1('10-medium.txt')
    220
    >>> part_1('10.txt')
    2046
    '''
    joltages = parse_input(filename)
    # Add the outlet socket joltage (0) and the device joltage (max+3)
    sorted_joltages = [0] + sorted(joltages) + [max(joltages)+3]
    diffs = Counter()
    for i in range(1, len(sorted_joltages)):
        diffs[sorted_joltages[i]-sorted_joltages[i-1]] += 1
    return diffs[3]*diffs[1]

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else '10.txt'
    logging.basicConfig(level='WARN') # Set to INFO for debugging
    print(part_1(filename))

