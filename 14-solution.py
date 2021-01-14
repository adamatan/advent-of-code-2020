import fileinput
import re

def parse_mask(mask):
    zero_mask = ''.join(['0' if c == '0' else '1' for c in mask])
    one_mask = ''.join(['1' if c == '1' else '0' for c in mask])
    return int(zero_mask,2), int(one_mask, 2)

def apply_mask(mask, number):
    return (number & mask[0]) | mask[1]

mem = {}

def day_1():
    '''
    >>> day_1()
    9296748256641
    '''
    with fileinput.input('14.txt') as f:
        for line in f:
            if 'mask' in line:
                mask = parse_mask(line.split('=')[1].strip())
            else:
                address, number = re.findall(r'mem\[(\d+)\]\s+\=\s+(\d+)', line)[0]
                address, number = int(address), int(number)
                mem[address] = apply_mask(mask, number)
    return sum(mem.values())

if __name__ == '__main__':
    print(day_1())
