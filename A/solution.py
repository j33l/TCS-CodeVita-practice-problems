#
# Solution for "A Board Game"
#

import numpy as np

# input

N = input('enter grid size: ')

print('enter grid values... \n')
row1 = [int(i) for i in input().split()]
row1[0] = 0 # making top-left value 0 implecitly of user input
row2 = [int(i) for i in input().split()]
row3 = [int(i) for i in input().split()]

grid = [row1, row2, row3]

# display grid input

print(np.matrix(grid))

# finding smallest route

s = grid[0][0] # score

s = s/2 + k

if grid[0][1] < grid[1][0]:
    move('right')
elif grid[0][1] > grid[1][0]:
    move('down')
else: # both are equal then find which will be best move, by comparing next of next move
    
