#
# Solution for "B - Paper Generation"
#

import string
from itertools import permutations, combinations, chain
# reference: https://www.geeksforgeeks.org/permutation-and-combination-in-python/
# comb = combinations([2, 1, 3], 2)
# perm = permutations([1, 2, 3], 2)
# for i in list(perm): 
#     print i 

# user input
ts = int(input('Enter number TOTAL SIMPLE queasion: '))
ss = int(input('Enter number SELECTED SIMPLE queasion: '))

tm = int(input('Enter number TOTAL MEDIUM queasion: '))
sm = int(input('Enter number SELECTED MEDIUM queasion: '))

tc = int(input('Enter number TOTAL COMPLEX queasion: '))
sc = int(input('Enter number SELECTED COMPLEX queasion: '))

# checking for constrains
if ss < 1 or sm < 1 or sc < 1:
    print('Should include every type of question at least once!')
    exit()

if (ts < ss) or (tm < sm) or (tc < sc):
    print('Should select less or equel to number of available queations!')
    exit()

if (ss + sm + sc) > 24 or (ss + sm + sc) < 1:
    print('Should include minimum 3 and maximum 24 questions in each paper!')
    exit()

# total possible question paper without any constrains
# tp = ss * sm * sc # total paper possible // before, maybe incorrect
tp = ts * tm * tc # total paper possible
tq = ss + sm + sc # total questions per paper

print('\nNumber of totoal possible question papers is: ', str(tp))
print('Number of totoal  question in each papers is: ', str(tq))

# printing all questions indicators
tqs = ts + tm + tc # total questions available
qi = [] # questions indicators
for i in range(97, 97 + tqs):
	qi.append(chr(i).upper())
print('\nAll question indicators... \n')
print(qi)

simpleQueIndi = [] # simple questions indicators
for i in range(97, 97 + ts):
	simpleQueIndi.append(chr(i).upper())
print('Simple question indicators... \n')
print(simpleQueIndi)

mediumQueIndi = [] # medium questions indicators
for i in range(97 + ts, 97 + ts + tm):
	mediumQueIndi.append(chr(i).upper())
print('Medium question indicators... \n')
print(mediumQueIndi)

complexQueIndi = [] # complex questions indicators
for i in range(97 + ts + tm, 97 + ts + tm + tc):
	complexQueIndi.append(chr(i).upper())
print('Complex question indicators... \n')
print(complexQueIndi)

# printing possible questions pairs for papers without constrains
aqc = [] # all questions combinations

# combinations
simpleComb = list(combinations(simpleQueIndi, ss))
for i in simpleComb: 
	aqc.append(i)
print('Simple question combinations... \n')
print(simpleComb)

mediumComb = list(combinations(mediumQueIndi, sm))
for i in mediumComb: 
	aqc.append(i)
print('Medium question combinations... \n')
print(mediumComb)

complexComb = list(combinations(complexQueIndi, sc))
for i in complexComb: 
	aqc.append(i)
print('Complex question combinations... \n')
print(complexComb)

# combining questions for final paper
ans = [] # final paper list
for s in simpleComb:
	for m in mediumComb:
		for c in complexComb:
			ans.append(list(chain(s, m, c)))

print('-----', str(len(ans)), ' : paper list ----- \n')
for paperQueList in ans:
    print(paperQueList, end="\n")
print('--------------------------------- \n')

# selecting which two questions can't come in same paper
qs = [q.upper() for q in input('Enter which questions can not be in same paper:').split()]
print('Questions ', qs[0], qs[1], ' will not come in same paper.')

# selecting question which can be placed in one paper
q = input('Enter question which can be placed in one paper: ').upper()
print('Question', q, ' will be only in one paper.')

# applying constrains of questions
finalAns = []
isOnlyOne = False

for paperItem in ans:
    if (qs[0] in paperItem) and (qs[1] in paperItem):
        continue
    if (q in paperItem) and (isOnlyOne == True):
        continue
    if (q in paperItem) and (isOnlyOne == False):
        isOnlyOne = True
    finalAns.append(paperItem)

for paperQueList in finalAns:
    print(paperQueList, end="\n")
print(str(len(finalAns)))
