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
queryArr = [
    int(input('Enter query (1 based index number): ')) - 1
    for _ in range(queryNumb)
]


# triming givenStr as per strLen
del givenStrAsList[strLen:]

presentIndexList = []

# finding all occurance of given char in given list
allIndexPosList = [
    list(locate(givenStrAsList, lambda x: x == givenStrAsList[i]))
    for i in queryArr
]

# finding preceeding occurance of given char in given list
preceedingIndexList = [
    list(filter(lambda x: (x < queryArr[i]), allIndexPosList[i]))
    for i in range(queryNumb)
]


print('All matching index: ', allIndexPosList)
print('Preceeding imdex: ', preceedingIndexList)

# number of occurrence of same alphabet preceding
ansLen = [len(i) for i in preceedingIndexList]

print('\nNumber of occurrence', ansLen)
