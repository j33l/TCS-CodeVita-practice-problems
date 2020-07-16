'''
Solution for "Lifeguard Prob"
'''

import math
import numpy as np

#
# User input
#

'''
All coordinates values are integer as per problem description
'''
# x_lifeGuard = int(input('Enter x for life guard: '))
# y_lifeGuard = int(input('Enter y for life guard: '))
# x_drowning = int(input('Enter x for drowning person: '))
# y_drowning = int(input('Enter y for drowning person: '))
# multiplyingFactor  = float(input('Enter multiplying factor for life guard: '))

'''
static input for testing
'''
x_lifeGuard = 1
y_lifeGuard = 1
x_drowning = 1
y_drowning = -1
multiplyingFactor  = 1.2

# assuming other factors
lifeGuardVelocity = 10

'''
Calculates distance between two poinds on 2D plane
arguments: 1=x position of point1, 2=y position of point1, 2=x position of point2, 3=y position of point2
returns float (based on unit of coordinate system)
'''
def calcDistance(x1, y1, x2, y2):
    # return math.sqrt(math.pow(x - x1, 2) + math.pow(y - y1, 2) * 1.0) 
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)) 

'''
Calculates time based on Velocity and Distance
arguments: 1=velocity, 2=distance
returns float (based on unit of velocity)
'''
def calcTime(velocity, distance):
    return distance/velocity

'''
Calculating intersection of line formed by life guard and person
using formula `y - y1 = m (x - x1) ; m = (y2 - y1) / (x2 - x1)`
'''
xStraightIntersection = x_lifeGuard # if slop is 0, when person is straight front to the guard
if ((x_drowning - x_lifeGuard) != 0):
    xStraightIntersection = x_lifeGuard - (y_lifeGuard / ((y_drowning - y_lifeGuard) / (x_drowning - x_lifeGuard)))    

'''
calculating time taken by lifeguard for every case with 6 decimal points accuracy
'''
times, xOptimumRange = [], []
change = 0.000001 if x_drowning > x_lifeGuard else -0.000001 # based on lifeguard should run left ot right
# xFloatValues = list(np.linspace(xStraightIntersection, float(x_drowning), change))
xFloatValues = np.linspace(xStraightIntersection, float(x_drowning))
for xOptimum in xFloatValues:
    time = 0
    time += calcTime(lifeGuardVelocity * multiplyingFactor, calcDistance(xOptimum, x_lifeGuard, 0, y_lifeGuard)) # on ground
    time += calcTime(lifeGuardVelocity, calcDistance(xOptimum, x_drowning, 0, y_drowning)) # on waater
    times.append(time)
    xOptimumRange.append(xOptimum)

optimumXValue = xOptimumRange[times.index(min(times))]

print(optimumXValue)
