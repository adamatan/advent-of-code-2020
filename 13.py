'''
Solution for Advent of Code 2020, Day 13.
https://adventofcode.com/2020/day/13
Adam Matan <adam@matan.name>, 2021
'''

import sys
import logging


def get_input(input_filename):
    '''Parses the input file into a { timestamp: number, bus_lines:[] } dictionary.
    >>> get_input('13-small.txt')
    {'timestamp': 939, 'bus_lines': [7, 13, 59, 31, 19]}
    '''
    with open(input_filename) as f:
        timestamp, bus_lines = f.readlines()
        timestamp = int(timestamp)
        bus_lines = [int(i) for i in bus_lines.split(',') if i != 'x']
    return {'timestamp': timestamp, 'bus_lines': bus_lines}

def wait_time(timestamp, bus_line):
    if timestamp % bus_line == 0:
        return 0
    else:
        return (bus_line*(timestamp//bus_line)+bus_line)-timestamp

def part_1(filename):
    '''
    >>> part_1('13-small.txt')
    295
    '''
    parsed_ibput = get_input(filename)
    timestamp, bus_lines = parsed_ibput['timestamp'], parsed_ibput['bus_lines']
    lowest_wait_time, best_bus = float('inf'), None
    for bus_line in bus_lines:
        if (current_wait_time := wait_time(timestamp, bus_line)) < lowest_wait_time:
            lowest_wait_time, best_bus = current_wait_time, bus_line
    return best_bus * lowest_wait_time

def part_2(filename):
    '''
    >>> part_2('template.txt')
    True
    '''
    _ = get_input(filename)
    return True

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else '13.txt'
    logging.basicConfig(level='INFO') # Set to INFO for debugging

    print(part_1(filename))
    # print(part_2(filename))

