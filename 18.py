'''
Search and replace 'template' to adapt.

Solution for Advent of Code 2020, Day 18.
https://adventofcode.com/2020/day/18
Adam Matan <adam@matan.name>, 2021
'''
import re
import sys
import logging

parens_expression = re.compile(r'\([^\(]*?\)')

def solve(expression, depth):
    indent = '\t' * depth
    logging.info(f'{indent} expression: {expression}')
    expression = expression.replace(' ', '')
    if '(' not in expression:
        logging.info('Returing X')
        return 'X'
    while match := parens_expression.search(expression):
        logging.info(expression)
        inner_expression = expression[match.start():match.end()]
        logging.info(f'inner: {inner_expression}')
        replace = solve(inner_expression[1:-1], depth+1)
        logging.info(f'Replace: {replace}')
        expression = expression.replace(inner_expression, replace)
    return expression
    
def part_1(filename):
    '''
    >>> part_1('template.txt')
    True
    '''
    expression = '(8 + 4 + 9 + (7 * 9 + 4 + 6 + 9) * 3) + 6 + 5 + ((8 * 2) + 2 * 9) * 5'
    return solve(expression, depth=0)
    return False
    

def part_2(filename):
    '''
    >>> part_2('template.txt')
    True
    '''    
    return True

if __name__ == '__main__':
    # filename = sys.argv[1] if len(sys.argv) > 1 else '18.txt'
    logging.basicConfig(level='INFO') # Set to INFO for debugging
    print(part_1('x'))
    # print(part_2(filename))

