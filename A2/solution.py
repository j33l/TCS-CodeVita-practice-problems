#
# Solution for "Philaland Coin" problem
#

# N = [] # Max price array
# minimulCoins = [1] # minimal coin includes $1

# # user inputs
# for i in range(int(input())):
#     N.append(int(input()))

# for maxPrice in N:
#     if(maxPrice > 1):

# def multiples(m, count):
#     for i in range(1, count):
#         print(i*m)

# multiples(5, 5)

# reference : https://stackoverflow.com/questions/10035752/elegant-python-code-for-integer-partitioning
def partition(number):
    answer = {(number, )}
    for x in range(1, number):
        for y in partition(number - x):
            answer.add(tuple(sorted((x, ) + y)))
    return answer

# TODO: filter all 1's and number itself from set

partitionsSet = partition(4)

