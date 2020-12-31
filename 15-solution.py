
starting_numbers = [18,8,0,5,4,1,20]
starting_numbers = [0,3,6]

numbers = {}
for index, number in enumerate(starting_numbers):
    numbers[number] = index + 1

counter = len(numbers)
for number in starting_numbers:
    print(number, numbers[number])

while counter < 10:
    if number not in numbers or numbers[number] == counter:
        numbers[number] = counter
        print(f'Saying 0: {number} is first timer, counter={counter}, numbers={numbers}')
        number = 0
    else:
        print(f'Saying {counter - numbers[number]}: {number} has been seen at position {numbers[number]}, counter is {counter}, {numbers}')
        numbers[number] = counter - numbers[number]
        number = numbers[number]
    counter += 1

print()
print(number, counter)
