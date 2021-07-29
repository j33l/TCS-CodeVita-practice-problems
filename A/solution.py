#
# Solution for "A Board Game"
# Using path find algo.s, so we can find best possible solution, even at a time next move seems more valuable than other
#

from itertools import permutations
from math import floor

# input
n = int(input('Enter grid size: '))
moveList = []

print('Enter grid values...')
grid = [[int(i) for i in input().split()] for _ in range(n)]
grid[0][0] = 0 # making top-left value 0 implecitly of user input

# generating move list
for _ in range(n - 1):
    moveList.append('i')
    moveList.append('j')

# # static input
# grid = [[0, 1, 8, 8],
#         [9, 9, 9, 9],
#         [1, 9, 9, 9],
#         [1, 1, 1, 5]]
# grid = [[0, 1, 3, 8],
#         [9, 4, 4, 5],
#         [1, 6, 2, 7],
#         [1, 1, 1, 5]]

# move variables
possibleWays = list(set(permutations(moveList))) # converting into set to make only unique values available
possibleWaysSum = []

# print(possibleWays)

for way in possibleWays:
        i, j, tempSum = 0, 0, 0 # down=i, right=j

        for move in way:
                if move == 'i':
                        i += 1
                else:
                        j += 1
                # tempSum += grid[i][j]
                tempSum = floor(tempSum / 2) + grid[i][j] # new sum Calculation formula as per problem description

        possibleWaysSum.append(tempSum)

minWayIndex = possibleWaysSum.index(min(possibleWaysSum))

for i in grid:
        print(i)
print('i = down, j = right')
print('Minimum Value Path:', possibleWays[minWayIndex])
print('Minimum value:', min(possibleWaysSum))
