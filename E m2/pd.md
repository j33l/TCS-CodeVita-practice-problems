Grooving Monkeys
Problem Description
N monkeys are invited to a party where they start dancing. They dance in a circular formation, very similar to a Gujarati Garba or a Drum Circle. The dance requires the monkeys to constantly change positions after every 1 second.

The change of position is not random & you, in the audience, observe a pattern. Monkeys are very disciplined & follow a specific pattern while dancing.

Consider N = 6, and an array monkeys = {3,6,5,4,1,2}.

This array (1-indexed) is the dancing pattern. The value at monkeys[i], indicates the new of position of the monkey who is standing at the ith position.

Given N & the array monkeys[ ], find the time after which all monkeys are in the initial positions for the 1st time.

Constraints
1<=t<=10 (test cases)

1<=N<=10000 (Number of monkeys)

Input Format
First line contains single integer t, denoting the number of test cases.

Each test case is as follows -

Integer N denoting the number of monkeys.

Next line contains N integer denoting the dancing pattern array, monkeys[].

Output
t lines,

Each line must contain a single integer T, where T is the minimum number of seconds after which all the monkeys are in their initial position.

Timeout
1

Explanation
Example 1

Input

1

6

3 6 5 4 1 2

Output

6

Explanation

Consider N = 6, and an array monkeys = {3,6,5,4,1,2}.

Suppose monkeys are a,b,c,d,e,f, & Initial position (at t = 0) -> a,b,c,d,e,f

At t = 1 -> e,f,a,d,c,b

a will move to 3rd position, b will move to 6th position, c will move to 5th position, d will move to 4th position, e will move to 1st position and f will move to 2nd position. Thus from a,b,c,d,e,f at t =0, we get e,f,a,d,c,b at t =1. Recursively applying same transpositions, we get following positions for different values of t.

At t = 2 -> c,b,e,d,a,f

At t = 3 -> a,f,c,d,e,b

At t = 4 -> e,b,a,d,c,f

At t = 5 -> c,f,e,d,a,b

At t = 6 -> a,b,c,d,e,f

Since at t = 6, we got the original position, therefore the answer is 6.