#
# Solution for "Lexicographical String"
#

# user inputs
testNumb = int(input('Enter number of test cases: '))
givenOrderArr = []
givenStrArr = []

for i in range(testNumb):
    givenOrderArr.append(input('Enter string for the new order of letters in the English dictionary: '))
    givenStrArr.append(input('Enter string to sort by previously specified order: '))

# sorting strings
sortedStrArr = []

def sortBySpecificOrder(myStr, myOrder):
    return sorted(myStr, key=lambda word: [myOrder.index(c) for c in word])

for i in range(testNumb):
    sortedStrArr.append(sortBySpecificOrder(givenStrArr[i], givenOrderArr[i]))

def convertListToStr(s): 
    # initialization of string to "" 
    tmpStr = "" 
    # using join function join the list s by separating words by str1 
    return tmpStr.join(s)

sortedStrArr = [convertListToStr(i) for i in sortedStrArr]

print('Input: ', givenStrArr)
print('Sorted: ', sortedStrArr)
