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

# all questions combinations
aqc = []

# combinations
simpleComb = list(combinations(simpleQueIndi, ss))
for i in simpleComb: 
	aqc.append(i)
	# print(i)

mediumComb = list(combinations(mediumQueIndi, sm))
for i in mediumComb: 
	aqc.append(i)
    # print(i)

complexComb = list(combinations(complexQueIndi, sc))
for i in complexComb: 
	aqc.append(i)
    # print(i)

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
