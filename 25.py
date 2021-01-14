import sys
import fileinput

DIVIDER = 20201227
SUBJECT_NUMBER = 7
MAX_LOOP_SIZE = 1e7

def calculate_loop_size(public_key):
    loop_count, value = 0, 1
    while value != public_key and loop_count < MAX_LOOP_SIZE:
        value = (value * SUBJECT_NUMBER) % DIVIDER
        loop_count += 1
    return loop_count

def generate_encryption_key(loop_size, public_key):
    value = 1
    for i in range(loop_size):
        value = (value * public_key) % DIVIDER
    return value

def part_1(filename):
    '''
    >>> part_1('25.txt')
    15380989
    >>> part_1('25-small.txt')
    14897079
    '''
    with fileinput.input(filename) as f:
        card_public_key, door_public_key = int(f.readline()), int(f.readline())

    card_loop_size = calculate_loop_size(card_public_key)
    return generate_encryption_key(card_loop_size, door_public_key)

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else '25.txt'
    print(part_1(filename))
