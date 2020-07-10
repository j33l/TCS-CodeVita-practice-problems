#
# Solution for "Prime Fibonnaci"
# Dependencies : pip install sympy itertools
#

from sympy import primerange, isprime
# from itertools import combinations
from itertools import permutations 

# User input
print('Enter two numbers separated by space: ')
n1, n2 = [int(i) for i in input().split(' ')]

# Calculating all prime numbers between n1 and n2
primeNumList1 = list(primerange(n1, n2 + 1))

print('Prime numbers : ', primeNumList1)

# Generating unique combinations
primeNumList1Permutations = list(set([int(str(i[0])+str(i[1])) for i in list(permutations(primeNumList1, 2))])) # converting into set to make only unique values available

print('Prime numbers combinations : ', primeNumList1Permutations)

# filtering prime numbers
primeNumList2 = list(filter(lambda x: isprime(x) , primeNumList1Permutations))

print('Prime nubmers in Combinations : ', primeNumList2)

minPrime, maxPrime, countPrime = min(primeNumList2), max(primeNumList2), len(primeNumList2)

print(f'MaxPrime = {maxPrime}, minPrime = {minPrime}, count of primenumbers = {countPrime}')

# Generating Fibonacci series
FibArray = [minPrime, maxPrime] # first two fibonacci numbers

# Function for n-th fibonacci number - Dynamic Programing 
def fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    elif n<=len(FibArray): 
        return FibArray[n-1] 
    else: 
        temp_fib = fibonacci(n-1)+fibonacci(n-2) 
        FibArray.append(temp_fib) 
        return temp_fib 

print(f'{countPrime}th Fibonacci number in the series that has {minPrime} and {maxPrime} as the first 2 numbers is ',fibonacci(countPrime))
