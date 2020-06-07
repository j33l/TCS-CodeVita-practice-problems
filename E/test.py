# custom sorting test

givenStr = 'ativedoc'
givenOrder = 'qwryupcsfoghjkldezxvbintma'

sortedList = sorted(givenStr, key=lambda word: [givenOrder.index(c) for c in word])

print(sortedList)
