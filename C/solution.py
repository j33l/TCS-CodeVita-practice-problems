#
# Solution for "New ATM Design"
#

import math
import string

# Currency note counters
N100 = 0
N200 = 0
N500 = 0
N1000 = 0

# user input
N = int(input('Enter maximum withdrawal currency notes at a time: '))
withdrawAmount = int(input('Amount you want to withdraw (in multiples of 100): '))
TN100 = int(input('Available currency note of Rs 100 in the ATM: '))
TN200 = int(input('Available currency note of Rs 200 in the ATM: '))
TN500 = int(input('Available currency note of Rs 500 in the ATM: '))
TN1000 = int(input('Available currency note of Rs 1000 in the ATM: '))

# # counting possible notes, minimum notes
# while withdrawAmount >= 1000 and N1000 <= TN1000:
#     N1000 += 1
#     withdrawAmount -= 1000
# while withdrawAmount >= 500 and N500 <= TN500:
#     N500 += 1
#     withdrawAmount -= 500
# while withdrawAmount >= 200 and N200 <= TN200:
#     N200 += 1
#     withdrawAmount -= 200
# while withdrawAmount >= 100 and N100 <= TN100:
#     N100 += 1
#     withdrawAmount -= 100

# counting possible notes, maximum notes
while withdrawAmount >= 100 and N100 <= TN100:
    N100 += 1
    withdrawAmount -= 100
while withdrawAmount >= 200 and N200 <= TN200:
    N200 += 1
    withdrawAmount -= 200
while withdrawAmount >= 500 and N500 <= TN500:
    N500 += 1
    withdrawAmount -= 500
while withdrawAmount >= 1000 and N1000 <= TN1000:
    N1000 += 1
    withdrawAmount -= 1000

if withdrawAmount > 0:
    print("Invalid input! Do not insert a decimal. Enter in multiples of 100 only.")
    print('Can not provide ', str(withdrawAmount), ' Rs, which is < 100.')
    exit()

numbNotes = N1000 + N500 + N200 + N100 # total currency notes
if N < numbNotes:
    print('Can not provide currency notes as per withdrawal limit!')
    exit()

# printing output
print('\n You will have total ', str(numbNotes), 'currency Notes, as... \n')
if N1000 > 0:
    print(str(N1000), '1000 notes', end="\n")
if N500 > 0:
    print(str(N500), '500 notes', end="\n")
if N200 > 0:
    print(str(N200), '200 notes', end="\n")
if N100 > 0:
    print(str(N100), '100 notes', end="\n")
