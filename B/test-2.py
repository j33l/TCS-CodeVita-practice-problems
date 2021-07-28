# combining multiple lists

from itertools import chain 

simple = [('A', 'B'), ('A', 'C'), ('B', 'C')]
medium = [('D', 'E', 'F'), ('D', 'E', 'G'), ('D', 'F', 'G'), ('E', 'F', 'G')]
complexs = [('H', 'I'), ('H', 'J'), ('I', 'J')]

qs = ['A', 'D']
onlyOne = 'G'

all = []

x = []

for s in simple:
    for m in medium:
        for c in complexs:
            # x.extend(s)
            # x.extend(m)
            # x.extend(c)
            # all.append(x)
            # x = []
            all.append(list(chain(s, m, c)))

for paperQueList in all:
    print(paperQueList, end="\n")
print(str(len(all)))

# applying constrains of questions
finalAns = []
isOnlyOne = False

for paperItem in all:
    if (qs[0] in paperItem) and (qs[1] in paperItem):
        continue
    if onlyOne in paperItem and isOnlyOne:
        continue
    if onlyOne in paperItem:
        isOnlyOne = True
    finalAns.append(paperItem)

for paperQueList in finalAns:
    print(paperQueList, end="\n")
print(str(len(finalAns)))
