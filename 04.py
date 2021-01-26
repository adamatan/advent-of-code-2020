'''
Solution for Advent of Code 2020, Day 4.
https://adventofcode.com/2020/day/4
Adam Matan <adam@matan.name>, 2021
'''

import re
import sys
import logging



def parse_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    passports_as_strings = raw_input.split('\n\n')
    reg = re.compile(r'(\S+)\:(\S+)', re.MULTILINE)
    passports = [dict(reg.findall(passport)) for passport in passports_as_strings]
    return passports


def has_all_fields(passport):
    """
    >>> has_all_fields({'ecl': 'brn', \
                        'pid': '737531770', \
                        'iyr': '2010', \
                        'eyr': '2020', \
                        'byr': '1929', \
                        'hgt': '189cm', \
                        'hcl': '#c0946f'})
    True
    >>> has_all_fields({'ecl': 'brn', 'pid': '737531770', 'iyr': '2010', 'eyr': '2020'})
    False
    """
    REQUIRED_FIELDS = {'hcl', 'hgt', 'byr', 'iyr', 'pid', 'eyr', 'ecl'}
    return REQUIRED_FIELDS.issubset(set(passport.keys()))

def is_field_valid(field, value):
    """
    >>> is_field_valid('hcl', '#12345a')
    True

    >>> is_field_valid('hcl', '12345678')
    False

    >>> is_field_valid('pid', '012345678')
    True

    >>> is_field_valid('pid', 'x')
    False

    >>> is_field_valid('byr', '1930')
    True

    >>> is_field_valid('byr', '2020')
    False

    >>> is_field_valid('iyr', '2015')
    True

    >>> is_field_valid('iyr', '2000') == is_field_valid('iyr', '3000') == False
    True

    >>> is_field_valid('eyr', '2021')
    True

    >>> is_field_valid('eyr', '2040')
    False
    """

    if field == 'hcl':
        return bool(re.match(r'#[0-9a-f]{6}', value))
    elif field == 'pid':
        return bool(re.match(r'\d{9}', value))
    elif field == 'byr':
        return 1920 <= int(value) <= 2002
    elif field == 'iyr':
        return 2010 <= int(value) <= 2020
    elif field == 'eyr':
        predicate = 2020 <= int(value) <= 2030
        logging.warning(f'{field}, {value}, {predicate}')
        return predicate

    return False

def is_passport_valid(passport):
    if not has_all_fields(passport):
        return False
    for field, value in passport.items():
        if not is_field_valid(field, value):
            return False
    return True


def part_1(filename):
    '''
    >>> part_1('04.txt')
    206
    '''
    passports = parse_input(filename)
    valid_passports = [p for p in passports if has_all_fields(p)]
    return len(valid_passports)


def part_2(filename):
    # '''
    # >>> part_2('04.txt')
    # True
    # '''
    passports = parse_input(filename)
    valid_passports = [p for p in passports if is_passport_valid(p)]
    return len(valid_passports)

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else '04.txt'
    logging.basicConfig(level='WARN') # Set to INFO for debugging
    print(part_1(filename))
    print(part_2(filename))
