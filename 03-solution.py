import re
import math
from utils.utils import get_input_rows

input_rows = get_input_rows(__file__)

def is_tree(row, column, width, tree_map):
    return tree_map[row][column % width] == '#'

def part_1(rows, row_delta, column_delta):
    """Counts the number of trees in the path"""
    height, width = len(rows), len(rows[0])
    row, column, tree_count = 0, 0, 0
    while row < height:
        tree_count += is_tree(row, column, width, rows)
        row += row_delta
        column += column_delta
    return tree_count

def part_2(rows):
    slopes_text='''Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.'''
    slopes = [(int(row), int(col)) for (col, row) in re.findall('Right (\d), down (\d)', slopes_text)]
    tree_encounters = [part_1(rows, *slope) for slope in slopes]
    return math.prod(tree_encounters)

print(part_1(input_rows, 1, 3))
print(part_2(input_rows))