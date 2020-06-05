# Paper Generation

--> Problem Description
Ravi needs to set Question papers fairly for his students for an exam. He has three categories of Questions i.e. Simple, Medium,
Complex. Each Question paper has one or more simple, medium, complex questions.
For each paper, he needs to choose precisely s out of a set of x simple, precisely m out of a set of y medium and precisely c out of
a set of z complex questions.
These questions are labelled A, B, C and so on, with the first x being simple, the next y being medium and the last z being hard.

-> Write a program that prints the number of possible combination of Question papers

-> Ravi decides to impose following constraints while selecting the question papers:
- Two given questions can't come together in any Question paper
- One of the given Question can come in only one Question paper
- Remaining Questions can come any number of Question papers

-> Find how many Question papers can be generated after imposing the constraints.

--> Constraints
s,m,c > = 1

x > = s, y > = m, z > = c

1 < (s + m + c) < =26 
(where 26 is number of alphabet, A to Z)

--> Input Format
The First line contains x, the number of simple questions.
The Second line contains s, the number of simple questions to choose from x.

The Third line contains y, the number of medium questions.
The Fourth line contains m, the number of medium questions to choose from y.

The Fifth line contains z, the number of complex questions.
The Sixth line contains c, the number of complex questions to choose from z.

The Seventh line contains the question pair that cannot be the part of the same Question paper, delimited by single space.

The Eighth line contains the Question that should be asked only in one of the Question Papers.

--> Output
The First line contains total number of Question papers possible without any constraints.

The Second line contains total number of Question papers after imposing all the constraints.

# Time Limit
1

# Explanation
--> Example 1
-> Input

3

2

4

3

3

2

A D

G

-> Output

36

4

-> Explanation:

From the input we know that there are 3 simple, 4 medium and 3 complex questions.

First x as per the alphabetical order are simple questions, next y are medium questions and remaining z are complex questions.
The total number of Question papers that can be generated without imposing constraints is 36 (3*4*3=36).

As Questions A and D cannot be cannot be in the same Question Paper and Question G can exist only in one of the Question paper,
the maximum number of Question papers that can be generated after imposing constraints is 4 (36-).

And one of the possible set of 4 question papers is:

ABEFGHI

BCDEFHI

BCDEFHJ

BCDEFIJ

Example 2

Input

3

2

3

2

3

2

A C

D

Output

27

7

Explanation:

From the input we know that there are 3 simple, 3 medium and 3 complex questions.

First x as per the alphabetical order are simple Questions,next y are medium Questions and remaining z are complex Questions. The total number of Question papers that can be generated without imposing constraints is 27.

As Questions A and C cannot be cannot be in the same Question Paper and Question D can exist only in one of the Question paper, the maximum number of Question papers that can be generated after imposing constraints is 7.

And one of the possible sets of 7 question papers is:

ABDEGH

ABEFGH

ABEFGI

ABEFHI

BCEFGH

BCEFGI

BCEFHI