import re
import sys
import fileinput

def parse_ranges_line(line):
    '''
    >>> parse_ranges_line('row: 35-295 or 312-956')
    [(35, 295), (312, 956)]
    '''
    reg = re.compile('(\d+)\-(\d+)')
    line_ranges = reg.findall(line)
    line_ranges = [tuple(map(int, t)) for t in line_ranges]
    return line_ranges

def parse_ticket_line(line):
    '''
    >>> parse_ticket_line('729,389,377')
    [729, 389, 377]
    '''
    numbers = [int(i) for i in re.findall('\d+', line)]
    return numbers

def parse_input_file(filename):
    ranges = []
    numbers = []
    is_first_line = True
    with fileinput.input(filename) as f:
        for line in f:
            if 'or' in line:
                line_ranges = parse_ranges_line(line)
                ranges.extend(line_ranges)
            elif re.match('^\d+', line):
                if is_first_line:
                    is_first_line = False
                else:
                    numbers.extend(parse_ticket_line(line))
    return ranges, numbers

def part_1(filename):
    '''
    >>> part_1('16.txt')
    25788
    '''
    ranges, numbers = parse_input_file(filename)
    ticket_scanning_error_rate = 0

    for number in numbers:
        in_range = False
        for r in ranges:
            if r[0] <= number <= r[1]:
                in_range = True
                break
        if not in_range:
            ticket_scanning_error_rate += number

    return ticket_scanning_error_rate

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else '16.txt'
    print(filename)
    print(part_1(filename))

        
