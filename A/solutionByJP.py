#
# Solution for "A Board Game"
# My other attempt
# Now using "Greedy algo. technique"
#

from math import floor

# Static user inputs
# boardGrid = [[0, 3, 9, 6],
#             [1, 4, 4, 5],
#             [8, 2, 5, 4],
#             [1, 8, 5, 9]]
# boardGrid = [[0, 82, 2, 6, 7],
#             [4, 3, 1, 5, 21],
#             [6, 4, 20, 2, 8],
#             [6, 6, 64, 1, 8],
#             [1, 65, 1, 6, 4]]

# User inputs
boardGrid = []
gridSize = int(input('Enter size of grid: '))
for i in range(gridSize):
    print('Enter ', i, 'th row values separated by spaece: 4')
    boardGrid.append([int(i) for i in input().split()])

SIZE = len(boardGrid[0]) - 1
score = 0
nextPosition, previousPosition = 0, 0 #[0, 0], [0, 0]

i, j = 0, 0 # row, col
while(i != SIZE and j != SIZE): # till reached bottom right place (3, 3)
    if(boardGrid[i][j + 1] < boardGrid[i + 1][j]):
        j += 1
        print('right, ', end="")
    else:
        i += 1
        print('down, ', end="")
    score = floor(score / 2) + boardGrid[i][j]
    

score = floor(score / 2) + boardGrid[SIZE][SIZE] # adding last value

print('\nScore :', score)
