# A Board Game

--> Problem Description
You are given an N x N grid of squares. Each square except the top left is filled with a positive integer. You start at the top
left corner with a score of 0 and move to the bottom right square by moving either right by one square or down by one square. As
you move to the new square, your score becomes `[S/2] + k`, where `S` was the score at your previous square and k is the number 
written in the current square. In the above, [x] is the largest integer which is not greater than x. Thus, [5] is 5, and [5.5] is 
also 5.
Write a program to find the smallest score with which you can exit the grid.

--> Constraints
4 <= N <= 30
Number in each square <= 1000

--> Input Format
The first line contains a single integer N, representing the size of the grid
The next N lines, each having N space separated integers giving the numbers written on successive rows of the grid

--> Output
The smallest score with which you can exit the grid

--> Time Limit
1

## Explanation

-->Example 1
-> Input
4

0 3 9 6

1 4 4 5

8 2 5 4

1 8 5 9

-> Output

12

-> Explanation

N=4. The set of scores are as given. The 4 X 4 scores look as follows

One possible set of moves are down, right, down, right, right, down.

The corresponding scores are 1, 4, 4, 7, 7, 12

--> Example 2

-> Input

5

0 82 2 6 7

4 3 1 5 21

6 4 20 2 8

6 6 64 1 8

1 65 1 6 4

-> Output

7

-> Explanation

One possible set of moves are "down, right, right, right, down, down, down, right"
