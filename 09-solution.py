from utils.utils import get_input_as_number_list

numbers = get_input_as_number_list(__file__)
PREAMBLE_SIZE = 25

def has_pair(number_sequence, expected_sum):
    candidates = set(number_sequence)
    while candidates:
        current_number = candidates.pop()
        if expected_sum-current_number in candidates:
            return True
    return False

for index in range(PREAMBLE_SIZE, len(numbers)):
    trailing_list = numbers[index-PREAMBLE_SIZE:index]
    current_number = numbers[index]
    if not has_pair(trailing_list, current_number):
        print(current_number)
        break