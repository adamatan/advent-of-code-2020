import re
from utils.utils import get_input_rows

rows = get_input_rows(__file__)

SHINY_GOLD = 'shiny gold'

reg = re.compile(r'''
    ([a-z][a-z\s]+?)        # Bag name
    \s                      # Space
    bag                     # the word bag (or bags) as a separator
    ''',
    re.VERBOSE)

bag_content = {}

for row in rows:
    bags_in_row = reg.findall(row)
    container_bag, contained_bags = bags_in_row[0], bags_in_row[1:]
    if 'contain no other' in contained_bags[0]:
        contained_bags = []
    bag_content[container_bag] = set(contained_bags)
    
def has_shiny_gold(bag_name):
    contained_bags = bag_content[bag_name]
    if SHINY_GOLD in contained_bags:
        return True
    for bag in contained_bags:
        if has_shiny_gold(bag):
            return True
    return False

print(bag_content)
print(sum([has_shiny_gold(bag) for bag in bag_content]))
print(has_shiny_gold('dim violet'))