# New ATM Design

--> Problem Description
Automated Teller Machine (ATM) is an electronic device that enables people to withdraw cash from their bank account.
Every ATM has a limit for number of currency notes (say N), it can give at a time.

-> A bank wants to design an ATM for school students. The unique feature of this ATM would be that it would always give
maximum number of currency notes possible, to make the students happy.  Available denomination of currency notes in the ATM
are 100, 200, 500, 1000

--> Constraints
- N < 100

--> Input Format
- First Line provides an integer, N
- Second Line provides an integer denoting the amount you want to withdraw (in multiples of 100)
- Third Line provides an integer denoting the available currency note of Rs 100 in the ATM
- Fourth Line provides an integer denoting the available currency note of Rs 200 in the ATM
- Fifth Line provides an integer denoting the available currency note of Rs 500 in the ATM
- Sixth Line provides an integer denoting the available currency note of Rs 1000 in the ATM

-> Output
One line containing the maximum number of currency note possible for the desired withdrawal amount.
Output should be 0 (zero) if transaction is not possible, for example if sufficient fund is not available in the ATM.

# Time Limit
1

# Explanation

--> Example 1

-> Input

10

1300

10

10 

10

10

-> Output

10

-> Explanation

Here, 7 * 100 + 3* 200 + 0*500 +0*1000 hence maximum possible currency = 10. 

--> Example 2

-> Input

5

1700

1

2

2

2

-> Output

3

-> Explanation

Here, 0 * 100  + 1 * 200 + 1 * 500 +1 * 1000 hence maximum possible currency = 3.
