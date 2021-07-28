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
qi = [chr(i).upper() for i in range(97, 97 + tqs)]
print(qi)

simpleQueIndi = [chr(i).upper() for i in range(97, 97 + ts)]
print(simpleQueIndi)

mediumQueIndi = [chr(i).upper() for i in range(97 + ts, 97 + ts + tm)]
print(mediumQueIndi)

complexQueIndi = [
    chr(i).upper() for i in range(97 + ts + tm, 97 + ts + tm + tc)
]
print(complexQueIndi)

# combinations
simpleComb = list(combinations(simpleQueIndi, ss))
# all questions combinations
aqc = [i for i in simpleComb]

mediumComb = list(combinations(mediumQueIndi, sm))
for i in mediumComb: 
	aqc.append(i)
complexComb = list(combinations(complexQueIndi, sc))
for i in complexComb: 
	aqc.append(i)
# print('all... \n')
# print(aqc)

# print('final possible papers...')
# app = combinations(aqc, 3)
# print(app)

# reference: http://code.activestate.com/recipes/496807-list-of-all-combination-from-multiple-lists/
# a = [[1,2],[3,4,5],[6],[7,8,9,10]]

# r=[[]]
# for x in a:
#     t = []
#         for y in x:
#             for i in r:
#                 t.append(i+[y])
#     r = t

# r = [ i + [y] for y in aqc for i in r ]

# print(r)

aqc = []
for s in simpleComb:
	for m in mediumComb:
		for c in complexComb:
			aqc.append([s, m, c])

print('-----', str(len(aqc)), ' : paper list ----- \n')
for paperQueList in aqc:
    print(paperQueList, end="\n")
