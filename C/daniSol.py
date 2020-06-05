"""
reference: https://www.daniweb.com/programming/software-development/threads/478015/atm-algorithm

withdraw_money()
a.  prompt user for a money amount in US Dollars (no cents, i.e. no fractional part allowed)
b.  print a preamble which says that user will see the breakdown of the money in banknotes
c.  print maximum number of $100 bills that can be given for the amount given by user
d.  print maximum number of $50 bills that can be given for the amount left over from previous step
e.  print maximum number of $20 bills that can be given for the amount left over from previous step
f.  print maximum number of $10 bills that can be given for the amount left over from previous step
g.  print maximum number of $5 bills that can be given for the amount left over from previous step
h.  print maximum number of $2 bills that can be given for the amount left over from previous step
i.  print maximum number of $1 bills that can be given for the amount left over from previous step
"""

import math
import string

def withdraw_money():
    withdraw = 0
    hundreds = 0
    fifty = 0
    twenty = 0
    ten = 0
    five = 0
    two = 0
    one = 0
    withdraw = int(input("Input the amount you would like to withdraw\n--> "))
    while withdraw >= 100:
        hundreds += 1
        withdraw -= 100
    while withdraw >= 50:
        fifty += 1
        withdraw -= 50
    while withdraw >= 20:
        twenty += 1
        withdraw -= 20
    while withdraw >= 10:
        ten += 1
        withdraw -= 10
    while withdraw >= 5:
        five += 1
        withdraw -= 5
    while withdraw >= 2:
        two += 1
        withdraw -= 2
    while withdraw >= 1:
        one += 1
        withdraw -= 1
    if withdraw < 1 and withdraw > 0:
        print("invalid input")
        print("do not insert a decimal")
        withdraw_money()
    print("Here is the bill breakdown for the amount input")
    print(hundreds, "number of 100s")
    print(fifty, "number of 50s")
    print(twenty, "number of 20s")
    print(ten, "number of 10s")
    print(five, "number of 5s")
    print(two, "number of 2s")
    print(one, "number of 1s")

withdraw_money()

"""
and what it is giving me...
>>>
Input the amount you would like to withdraw
--> 200.30
invalid input
do not insert a decimal
Input the amount you would like to withdraw
--> 253
Here is the bill breakdown for the amount input
2 number of 100s
1 number of 50s
0 number of 20s
0 number of 10s
0 number of 5s
1 number of 2s
1 number of 1s
Here is the bill breakdown for the amount input
2 number of 100s
0 number of 50s
0 number of 20s
0 number of 10s
0 number of 5s
0 number of 2s
0 number of 1s
"""
