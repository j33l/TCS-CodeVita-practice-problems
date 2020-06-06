#
# Solution for "Marathon Winner"
#

import statistics

# user input
numCandidates = int(input('Enter number of candidates: '))
totalSprintTime = int(input('Enter total time of Sprint (In seconds): '))
candidatesSprintData = []
candidateStepData = []
n = 0
while n < numCandidates:
    print('Enter sprint data for ', int(n + 1), 'th candidate: ')
    candidatesSprintData.append([int(i) for i in input().split()])
    candidateStepData.append(int(input('Enter step data for candidate: ')))
    n += 1

print('Sprint data: \n', candidatesSprintData)
print('Step data: \n', candidateStepData)

# checking lead after couple second
leadAfterCoupleSec = []

def leadCount(sec):
    leadAfterNSec = []
    for n in range(len(candidatesSprintData)):
        sum = 0
        for i in range(sec):
            sum += candidatesSprintData[n][i]
        leadAfterNSec.append(sum * candidateStepData[n])
    return leadAfterNSec

for i in range(2, totalSprintTime, 2):
    leadAfterCoupleSec.append(leadCount(i))

print('Lead data: \n', leadAfterCoupleSec) # [[12, 16, 12], [33, 38, 36], [54, 62, 84]]

# calculating winner
winnerInPeriod = []

for nThSecList in leadAfterCoupleSec:
    winnerInPeriod.append(1 + nThSecList.index(max(nThSecList)))

print('Winner data: \n', winnerInPeriod)

print('\nWinner is', str(statistics.mode(winnerInPeriod)), 'as leading more number of times.')
