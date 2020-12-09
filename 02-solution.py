import re

with open('02-input.txt') as f:
    lines = f.read()

rows = re.findall('(\d+)\-(\d+)\s+(\S):\s(\S+)', lines)

def part_1_predicate(row):
    min_count, max_count, letter, password = row
    return int(min_count) <= password.count(letter) <= int(max_count)

def part_2_predicate(row):
    lower_index, higher_index, letter, password = row
    return (password[int(lower_index)-1] == letter) ^ (password[int(higher_index)-1] == letter)

print(sum([part_1_predicate(row) for row in rows]))
print(sum([part_2_predicate(row) for row in rows]))