'''
Solution for Advent of Code 2020, Day 20.
https://adventofcode.com/2020/day/20
Adam Matan <adam@matan.name>, 2021
'''

import re
import sys
import logging
from collections import Counter

def parse_input(filename):
    '''
    >>> tiles = parse_input('20-small.txt')
    >>> sorted(tiles.keys())
    [1171, 1427, 1489, 1951, 2311, 2473, 2729, 2971, 3079]
    >>> sorted(tiles[2311])
    ['.#####..#.', '..###..###', '..##.#..#.', '...#.##..#']
    '''
    with open(filename) as f:
        raw_input = f.read()
    tiles_raw = re.findall(r'Tile \d+\:[\s\.\#]+', raw_input, re.MULTILINE)
    tiles = {}
    for t in tiles_raw:
        number = int(re.search(r'\d+', t.splitlines()[0]).group())
        tile = [t for t in t.splitlines()[1:] if t.strip()]
        top = tile[0]
        bottom = tile[-1]
        left = ''.join([t[0] for t in tile])
        right = ''.join([t[-1] for t in tile])
        tiles[number] = set((top, bottom, left, right))
    return tiles

def part_1(filename):
    '''
    # >>> part_1('20.txt')
    # True
    '''
    tiles = parse_input(filename)
    all_borders = Counter()
    for tile, tile_borders in tiles.items():
        all_borders.update(tile_borders)
        # logging.warning(f'{tile} {tile_borders}')
    for border in ['.#####..#.', '..###..###', '..##.#..#.', '...#.##..#']:
        logging.warning(f'{border} {all_borders[border]}')
        for tile in tiles:
            if border in tiles[tile]:
                logging.warning(f'{tile} {border}')

    logging.warning(tiles[3079]) # #..##.#...
    logging.warning(tiles[2311])

def part_2(filename):
    '''
    >>> part_2('20.txt')
    True
    '''
    _ = parse_input(filename)
    return True

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else '20-small.txt'
    logging.basicConfig(level='WARN') # Set to INFO for debugging
    print(part_1(filename))
    # print(part_2(filename))

