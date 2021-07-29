'''
Solution for "Collision Course" problem
'''


import math
from itertools import combinations

# User input
N = int(input('Enter number of cars: '))

'''
stores list of three float values [x coordinate, y coordinate, velocity]
'''
carsVector = [
    [float(i) for i in input('Enter x, y and v: ').split()] for _ in range(N)
]

# filtering out cars which are moving away from origin, negative velocity
carsVector = list(filter(lambda x: (x[2] >= 0), carsVector))

'''
Static user input for testing
'''
# N = 5
# carsVector = [
#     [5, 12, 1],
#     [16, 63, 5],
#     [-10, 24, 2],
#     [7, 24, 2],
#     [-24, 7, 2]
# ]

'''
Calculates distance from origin (0, 0)
arguments: 1=x position of point, 2=y position of point
returns float (based on unit of coordinate system)
'''
def calcDistance(x, y):
    # x1, y1 = 0, 0 # origin
    # return math.sqrt(math.pow(x - x1, 2) + math.pow(y - y1, 2) * 1.0) 
    # return math.sqrt(math.pow(x - x1, 2) + math.pow(y - y1, 2)) 
    return math.sqrt(math.pow(x, 2) + math.pow(y, 2)) 

'''
Calculates time based on Velocity and Distance
arguments: 1=velocity, 2=distance
returns float (based on unit of velocity)
'''
def calcTime(velocity, distance):
    return distance/velocity

'''
list of timings at which all filtered cars will be at origin
'''

carsTiming = [
    calcTime(carVector[2], calcDistance(carVector[0], carVector[1]))
    for carVector in carsVector
]

timingsCombination = list(combinations(carsTiming, 2))

'''
filtering only collision timings when two cars are at origin at same time
'''
collisionsList = list(filter(lambda x: (x[0] == x[1]), timingsCombination))

numberOfCollisions = len(collisionsList)

print(numberOfCollisions)
