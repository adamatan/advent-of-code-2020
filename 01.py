'''
Solution for Advent of Code 2020, Day 1.
https://adventofcode.com/2020/day/5
Adam Matan <adam@matan.name>, 2021
'''

import sys
import logging

def get_input(filename):
    with open(filename) as f:
        expenses = [int(s) for s in f.readlines()]
    return expenses

def part_1_naive(expenses):
    '''O(N^2) soution
    >>> part_1_naive(get_input('01.txt'))
    955584
    >>> part_1_naive(get_input('01-small.txt'))
    514579
    '''
    for i in expenses:
        for j in expenses:
            if i+j == 2020:
                return i*j
    raise ValueError('No match found')

def part_1_sets(expenses):
    '''O(N^2) soution
    >>> part_1_sets(get_input('01.txt')) == part_1_naive(get_input('01.txt'))
    True
    >>> part_1_sets(get_input('01-small.txt')) == part_1_naive(get_input('01-small.txt'))
    True
    '''
    expenses = set(expenses)
    while expenses:
        current_expense = expenses.pop()
        complement = 2020 - current_expense
        if complement in expenses:
            return current_expense * complement
    raise ValueError('No match found')

def part_2(expenses):
    '''
    >>> part_2(get_input('01.txt'))
    287503934
    >>> part_2(get_input('01-small.txt'))
    241861950
    '''
    for i in expenses:
        for j in expenses:
            for k in expenses:
                if i+j+k == 2020:
                    return i*j*k
    raise ValueError('No match found')

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else '01.txt'
    file_input = get_input(filename)
    logging.basicConfig(level='WARN') # Set to INFO for debugging
    print(part_1_naive(file_input), part_1_sets(file_input))
    print(part_2(file_input))

