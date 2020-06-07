#
# Solution for "Similar Char"
# Depencencies: 
#   -->> pip install more-itertools  
#

from more_itertools import locate

# user inputs
strLen = int(input('Enter length of string: '))
givenStrAsList = list(input('Enter string: '))
queryNumb = int(input('Enter number of query: '))
queryArr = []

for i in range(queryNumb):
    queryArr.append(int(input('Enter query (1 based index number): ')) - 1) # storing in 0-based index value

# triming givenStr as per strLen
del givenStrAsList[strLen:]

# finding all occurance of given char in given list
allIndexPosList = []
presentIndexList = []

#------------ not working for unknown reasons------------
# def giveAllMatchIndex(myList, myChar):
#     return list(locate(myList, lambda a: a == myChar)

# for i in queryArr:
#     # allIndexPosList.append(giveAllMatchIndex(givenStrAsList, givenStrAsList[qry]))
#----------------------------------------------

for i in queryArr:
    allIndexPosList.append(list(locate(givenStrAsList, lambda x: x == givenStrAsList[i])))

# finding preceeding occurance of given char in given list
preceedingIndexList = []

for i in range(queryNumb):
    # preceedingIndexList.append(list(locate(allIndexPosList[i], lambda x: x < queryArr[i])))
    preceedingIndexList.append(list(filter(lambda x: (x < queryArr[i]), allIndexPosList[i])))

print('All matching index: ', allIndexPosList)
print('Preceeding imdex: ', preceedingIndexList)

# number of occurrence of same alphabet preceding
ansLen = [len(i) for i in preceedingIndexList]

print('\nNumber of occurrence', ansLen)
