'''
Solution for Advent of Code 2020, Day 22.
https://adventofcode.com/2020/day/22
Adam Matan <adam@matan.name>, 2021
'''

import sys
import logging

def parse_input(filename):
    '''
    >>> parse_input('22-small.txt')
    ([9, 2, 6, 3, 1], [5, 8, 4, 7, 10])
    '''
    with open(filename) as f:
        lines = f.readlines()
    deck_1, deck_2 = [], []
    deck = deck_1
    for line in lines:
        if 'Player 2' in line:
            deck = deck_2
        try:
            deck.append(int(line))
        except ValueError:
            pass
    return deck_1, deck_2

def calculate_score(deck):
    '''
    >>> calculate_score([3, 2, 10, 6, 8, 5, 9, 4, 7, 1])
    306
    '''
    logging.info(deck)
    reversed_list = deck[::-1]
    factors = range(1, len(reversed_list)+1)
    factors_and_cards = list(zip(reversed_list, factors))
    score = sum([c[0]*c[1] for c in factors_and_cards])
    return score

def calculate_winning_deck_part_1(deck_1, deck_2):
    '''
    >>> calculate_winning_deck_part_1([9, 2, 6, 3, 1], [5, 8, 4, 7, 10])
    [3, 2, 10, 6, 8, 5, 9, 4, 7, 1]
    '''
    while deck_1 and deck_2:
        top_1, top_2 = deck_1[0], deck_2[0]
        deck_1, deck_2 = deck_1[1:], deck_2[1:]
        winner = deck_1 if top_1 > top_2 else deck_2
        winner.extend([max(top_1, top_2), min(top_1, top_2)])
    winner = deck_1 or deck_2
    return winner

def part_1(filename):
    '''
    >>> part_1('22-small.txt')
    306
    >>> part_1('22.txt')
    29764
    '''
    deck_1, deck_2 = parse_input(filename)
    winner = calculate_winning_deck_part_1(deck_1, deck_2)
    return calculate_score(winner)

def part_2(filename):
    '''
    >>> part_2('22.txt')
    True
    '''
    _, _ = parse_input(filename)
    return True

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else '22.txt'
    logging.basicConfig(level='WARN') # Set to INFO for debugging
    print(part_1(filename))
    print(part_2(filename))
