Death Battle
Problem Description
In a crossover fantasy universe, Houin Kyoma is up in a battle against a powerful monster Nomu that can kill him in a single blow. However being a brilliant scientist Kyoma found a way to pause time for exactly M seconds. Each second, Kyoma attacks Nomu with certain power, which will reduce his health points by that exact power. Initially Nomu has H Health Points. Nomu dies when his Health Points reach 0. Normally Kyoma performs Normal Attack with power A. Besides from Kyoma’s brilliance, luck plays a major role in events of this universe. Kyoma’s Luck L is defined as probability of performing a super attack. A super attack increases power of Normal Attack by C. Given this information calculate and print the probability that Kyoma kills Nomu and survives. If Kyoma dies print “RIP”.

Constraints
0 < T <= 50

1 <= A, H, C, L1, L2 <= 1000

1 <= M <= 20.

L1<=L2

Input Format
First line is integer T denoting number of test cases.

Each test case consist of single line with space separated numbers A H L1 L2 M C. Where luck L is defined as L1/L2. Other numbers are, as described above.

Output
Print probability that Kyoma kills Nomu in form P1/P2 where P1<=P2 and gcd(P1,P2)=1. If impossible, print “RIP” without quotes.

Timeout
1

Explanation
Example 1

Input

2

10 33 7 10 3 2

10 999 7 10 3 2

Output

98/125

RIP