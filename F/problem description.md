# Similar Char

Problem Description
Tahir and Mamta are woking in a project in TCS. Tahir being a problem solver came up with an interesting problem for his friend Mamta. 

Problem consists of a string of length N and contains only small case alphabets. 

It will be followed by Q queries, in which each query will contain an integer P (1<=P<=N) denoting a position within the string. 

Mamta's task is to find the alphabet present at that location and determine the number of occurrence of same alphabet preceding the given location P.

Mamta is busy with her office work. Therefore, she asked you to help her.

Constraints
1 <= N <= 500000

S consisting of small case alphabets

1 <= Q <= 10000

1 <= P <= N

Input Format
First line contains an integer N, denoting the length of string.

Second line contains string S itself consists of small case alphabets only ('a' - 'z').

Third line contains an integer Q denoting number of queries that will be asked.

Next Q lines contains an integer P (1 <= P <= N) for which you need to find the number occurrence of character present at the Pth location preceeding P.

Output
For each query, print an integer denoting the answer on single line.

Time Limit
1

Explanation
Example 1

Input

9

abacsddaa

2

9

3

Output

3

1

Explanation

Here Q = 2 

For P=9, character at 9th location is 'a'. Number of occurrences of 'a' before P i.e., 9 is three.

Similarly for P=3, 3rd character is 'a'. Number of occurrences of 'a' before P. i.e., 3 is one.
