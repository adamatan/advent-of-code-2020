with open('01-input.txt') as f:
    expenses = sorted([int(s) for s in f.readlines()])
print(expenses)

for i in expenses:
    for j in expenses:
        if i+j == 2020:
            print(i, j, i*j)

for i in expenses:
    for j in expenses:
        for k in expenses:
            if i+j+k == 2020:
                print(i, j, k, i*j*k)