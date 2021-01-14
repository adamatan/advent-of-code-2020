import re
import sys
import fileinput
from collections import defaultdict
import itertools
import logging

def part_1(filename):
    '''
    >>> part_1('21.txt')
    2061
    '''
    word_reg = re.compile('[a-z]+')
    might_contain_allergans = defaultdict(set)
    all_ingredients = []

    with fileinput.input(filename) as f:
        for line in f:
            ingredients, allergans = line.split('contains')
            ingredients = word_reg.findall(ingredients)
            all_ingredients.extend(ingredients)
            allergans = word_reg.findall(allergans)
            for allergan in allergans:
                if allergan in might_contain_allergans:
                    might_contain_allergans[allergan] = might_contain_allergans[allergan].intersection(ingredients)
                else:
                    might_contain_allergans[allergan].update(ingredients)
                logging.info(allergan, ingredients, might_contain_allergans[allergan])
                

    logging.info(might_contain_allergans)
    suspicious_ingredients = set(itertools.chain.from_iterable(might_contain_allergans.values()))
    logging.info(suspicious_ingredients)
    return len([i for i in all_ingredients if i not in suspicious_ingredients])

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else '21.txt'
    logging.basicConfig(level='WARN') # Set to INFO for debugging
    print(part_1(filename))

