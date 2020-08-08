'''
Solution for "Lazy Student" problem
'''
#
# User inputs
#

numberOfTestCases = int(input('Enter number of test cases: '))
# validating data for test cases
if( numberOfTestCases < 1):
    print('Enter 1 or more test cases!')
    exit()

'''
Contains three integers for "questions in question bank", "questions in paper", "questions can practice"
'''
testData = []
for i in range(numberOfTestCases):
    testData.append([int(data) for data in input('Enter "questions in question bank", "questions in paper", "questions can practice": ').split()])


for data in testData:
    # validating data for questions
    if(data[1] > data[0] and data[2] > data[0]):
        print('Enter valid data for number of questions!')
        exit()
    
    # calculating probability
    # print(data[2]*mulInv(q)) modulo 1000000007

print(testData)
