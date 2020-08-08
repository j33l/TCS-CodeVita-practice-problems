
import string

t = int(input())

cases = []
for n in range(t):
    number_of_monkies = int(input())
    pattern = [(int(i) - 1) for i in input().split()] # converting into 0 based index values
    # pattern = []
    # for i in range(number_of_monkies):
    #     pattern.append(int(input())- 1)
    cases.append([number_of_monkies, pattern])

'''
static input
'''
# cases = [[6, [2, 5, 4, 3, 0, 1]]] # 0 bases index val

def change_position(pattern, old_position):
    new_position = []
    for i in range(len(pattern)):
        new_position.append(old_position[pattern.index(i)])
    return new_position

for case in cases:
    n, pattern = case[0], case[1]
    
    count = 1
    
    init_monkies_position = list(string.ascii_lowercase[: n])
    monkies_position = change_position(pattern, init_monkies_position)
    
    while monkies_position != init_monkies_position:
        monkies_position = change_position(pattern, monkies_position)
        count += 1

    print(count)
