#
# to test logic
#

from itertools import permutations, combinations
# reference: https://www.geeksforgeeks.org/permutation-and-combination-in-python/
# comb = combinations([2, 1, 3], 2)
# perm = permutations([1, 2, 3], 2)

ts, tm, tc = 3, 4, 3
ss, sm, sc = 2, 3, 2

tqs = ts + tm + tc # total questions available

# questions indicators
qi = [] # questions indicators
for i in range(97, 97 + tqs):
	qi.append(chr(i).upper())
print(qi)

simpleQueIndi = []
for i in range(97, 97 + ts):
	simpleQueIndi.append(chr(i).upper())
print(simpleQueIndi)

mediumQueIndi = []
for i in range(97 + ts, 97 + ts + tm):
	mediumQueIndi.append(chr(i).upper())
print(mediumQueIndi)

complexQueIndi = []
for i in range(97 + ts + tm, 97 + ts + tm + tc):
	complexQueIndi.append(chr(i).upper())
print(complexQueIndi)

# combinations
simpleComb = combinations(simpleQueIndi, ss)
for i in list(simpleComb): 
    print(i)

mediumComb = combinations(mediumQueIndi, sm)
for i in list(mediumComb): 
    print(i)

complexComb = combinations(complexQueIndi, sc)
for i in list(complexComb): 
    print(i)
