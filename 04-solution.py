import re
from utils.utils import get_input_as_string

# Parse input
input_string = get_input_as_string(__file__)

# A list of
# hcl:#c0946f byr:1933 eyr:2025 pid:517067213 hgt:173cm
# ecl:hzl
# iyr:2018
passports_as_strings = input_string.split('\n\n')

reg = re.compile(r'(\S+)\:\S+', re.MULTILINE)

# For example:
# ['hcl', 'byr', 'eyr', 'pid', 'hgt', 'ecl', 'iyr']
passport_as_list_of_fields = [reg.findall(passport) for passport in passports_as_strings]


required_fields_raw = '''byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
'''

required_fields = set(re.findall(r'^(\S{3})', required_fields_raw, re.MULTILINE))
required_fields.remove('cid')

count = 0
for p in passport_as_list_of_fields:
    if required_fields.issubset(set(p)):
        count += 1

print(count)