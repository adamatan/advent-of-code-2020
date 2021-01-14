'''
Solution for Advent of Code 2020, Day 5.
https://adventofcode.com/2020/day/5
Adam Matan <adam@matan.name>, 2021
'''

def parse_boarding_pass(boarding_pass):
    '''Parse a boarding pass string into a (row, column) pair.
    >>> parse_boarding_pass('FBFBBFFRLR')
    (44, 5)
    '''
    rows = boarding_pass[:7]
    cols = boarding_pass[7:]

    rows = int(rows.replace('F', '0').replace('B', '1'), 2)
    cols = int(cols.replace('L', '0').replace('R', '1'), 2)

    return rows, cols

def seat_id(row, col):
    '''Parse a (row, col) tuple into a single numerical ticket id.
    >>> seat_id(44, 5)
    357
    '''
    return row * 8 + col

def part_1():
    '''What is the highest seat ID on a boarding pass?
    >>> part_1()
    976
    '''
    with open('05.txt') as f:
        return max([seat_id(*parse_boarding_pass(seat)) for seat in f.read().split()])

def part_2():
    '''What is the ID of your seat?
    >>> part_2()
    685
    '''
    with open('05.txt') as f:
        seats = {parse_boarding_pass(seat) for seat in f.read().split()}

    last_row = max([s[0] for s in seats])
    first_row = 1
    last_column = max([s[1] for s in seats])
    first_column = 0

    for row in range(first_row, last_row):
        for col in range(first_column, last_column):
            if (row, col) not in seats:
                return seat_id(row, col)
    
    raise ValueError('No seat found')

if __name__ == '__main__':
    print(part_1())
    print(part_2())
