import re
from collections import namedtuple

with open('02-input.txt') as f:
    lines = f.read()

rows = re.findall('(\d+)\-(\d+)\s+(\S):\s(\S+)', lines)

def part_1(rows):
    count = 0
    for row in rows:
        min_count, max_count, letter, password = row
        count += int(min_count) <= password.count(letter) <= int(max_count)
    return count

def part_2(rows):
    count = 0
    for row in rows:
        lower_index, higher_index, letter, password = row
        predicate = (password[int(lower_index)-1] == letter) ^ (password[int(higher_index)-1] == letter)
        if predicate:
            count += 1
    return count

print(part_1(rows))
print(part_2(rows))
