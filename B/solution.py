#
# Solution for "B - Paper Generation"
#

import string
from itertools import permutations, combinations
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
tp = ss * sm * sc # total paper possible
tq = ss + sm + sc # total questions per paper

print('Number of totoal possible question papers is: ', str(tp))
print('Number of totoal  question in each papers is: ', str(tq))

# printing all questions indicators
print('Possible questions indicators...')
tqs = ts + tm + tc # total questions available
qi = [] # questions indicators
for i in range(97, 97 + tqs):
	qi.append(chr(i).upper())
print(qi)

simpleQueIndi = [] # simple questions indicators
for i in range(97, 97 + ts):
	simpleQueIndi.append(chr(i).upper())
print(simpleQueIndi)

mediumQueIndi = [] # medium questions indicators
for i in range(97 + ts, 97 + ts + tm):
	mediumQueIndi.append(chr(i).upper())
print(mediumQueIndi)

complexQueIndi = [] # complex questions indicators
for i in range(97 + ts + tm, 97 + ts + tm + tc):
	complexQueIndi.append(chr(i).upper())
print(complexQueIndi)

# printing possible questions pairs for papers without constrains



# selecting which two questions can't come in same paper
qs = [q.upper() for q in input('Enter which questions can not be in same paper:').split()]
print('Questions ', qs[0], qs[1], ' will not come in same paper.')

# selecting question which can be placed in one paper
q = input('Enter question which can be placed in one paper: ').upper()
print('Question', q, ' will be only in one paper.')
