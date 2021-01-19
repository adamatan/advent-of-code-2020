'''
Solution for Advent of Code 2020, Day 18.
https://adventofcode.com/2020/day/18
Adam Matan <adam@matan.name>, 2021
'''

import re
import sys
import logging
import operator

parens_expression = re.compile(r'\([^\(]*?\)')

def to_int_if_possible(item):
    '''
    >>> to_int_if_possible('3')
    3
    >>> to_int_if_possible('X')
    'X'
    '''
    try:
        return int(item)
    except ValueError:
        return item

def get_input(input_filename):
    '''Parses the input file into a list of lists of tokens.
    >>> get_input('18-small.txt')[0]
    [2, '*', 3, '+', '(', 4, '*', 5, ')']
    '''
    with open(input_filename) as f:
        expressions = f.readlines()
        expressions_as_tokens = [tokenize(exp.strip()) for exp in expressions]
    return expressions_as_tokens

def tokenize(line):
    '''
    >>> tokenize('5 * 6 * 8 * (9 + 7 * 8 * 9) + 6 + 2')
    [5, '*', 6, '*', 8, '*', '(', 9, '+', 7, '*', 8, '*', 9, ')', '+', 6, '+', 2]
    '''
    line = line.replace(' ', '')
    split = re.split(r'([\+\*\(\)])', line)
    tokens = [to_int_if_possible(t) for t in split if t]
    logging.debug('Returning %s', tokens)
    return tokens

def solve(tokens):
    '''
    >>> solve(['(', '(', 2, '+', 4, '*', 9, ')', '*', '(', 6, '+', 9, '*', 8, '+', 6, ')',\
    '+', 6, ')', '+', 2, '+', 4, '*', 2])
    13632
    '''
    logging.info(tokens)
    while ')' in tokens:
        closing_parens_index = tokens.index(')')
        opening_parens_inedx = closing_parens_index
        while tokens[opening_parens_inedx] != '(':
            opening_parens_inedx -= 1
        tokens_in_paresns = tokens[opening_parens_inedx+1:closing_parens_index]
        tokens = tokens[:opening_parens_inedx] + [solve(tokens_in_paresns)] + tokens[closing_parens_index+1:]
        logging.info(tokens)
    while len(tokens) > 1:
        op = operator.add if tokens[1] == '+' else operator.mul
        logging.info(tokens)
        tokens = [op(tokens[0], tokens[2])] + tokens[3:]
    return tokens[0]

def solve2(tokens):
    '''
    >>> solve2([1, '+', '(', 2, '*', 3, ')', '+', '(', 4, '*', '(', 5, '+', 6, ')', ')'])
    51
    >>> solve2([5, '*', 9, '*', '(', 7, '*', 3, '*', 3, '+', 9, '*', 3, '+', '(', 8, '+', 6, '*', 4, ')', ')'])
    669060
    '''
    logging.info(tokens)
    while ')' in tokens:
        closing_parens_index = tokens.index(')')
        opening_parens_inedx = closing_parens_index
        while tokens[opening_parens_inedx] != '(':
            opening_parens_inedx -= 1
        tokens_in_paresns = tokens[opening_parens_inedx+1:closing_parens_index]
        tokens = tokens[:opening_parens_inedx] + [solve2(tokens_in_paresns)] + tokens[closing_parens_index+1:]
        logging.info(tokens)

    while '+' in tokens:
        index = tokens.index('+')
        tokens = tokens[:index-1] + [tokens[index-1]+tokens[index+1]] + tokens[index+2:]
        logging.info('+: %s', tokens)

    while '*' in tokens:
        index = tokens.index('*')
        tokens = tokens[:index-1] + [tokens[index-1]*tokens[index+1]] + tokens[index+2:]
        logging.info('*: %s', tokens)

    return tokens[0]


def part_1(input_filename):
    '''
    >>> part_1('18-small.txt')
    26335
    >>> part_1('18.txt')
    3348222486398
    '''
    input_as_tokens = get_input(input_filename)
    return sum([solve(token) for token in input_as_tokens])

def part_2(input_filename):
    '''
    >>> part_2('18-small.txt')
    693891
    >>> part_2('18.txt')
    43423343619505
    '''
    input_as_tokens = get_input(input_filename)
    return sum([solve2(token) for token in input_as_tokens])

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else '18.txt'
    logging.basicConfig(level='ERROR') # Set to INFO for debugging
    print(part_1(filename))
    print(part_2(filename))
