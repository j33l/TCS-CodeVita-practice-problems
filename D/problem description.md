# Marathon Winner

--> Problem Description
-> Race is generally organized by distance but this race will be organized by time.
In order to predict the winner we will check every 2 seconds.
Let's say total race time is 7 seconds we will check for (7-1) seconds.
For 7 sec : We will check who is leading at 2 sec, 4 sec and 6 sec.
Participant who is leading more number of times is winner from prediction perspective.

-> Now our task is to predict a winner in this marathon.

-> Note:
- 1) At particular time let say at 4th second, top two (top N, in general) participants are at same distance, then in this case both are leading we will increase count for both (all N).
- 2) And after calculating at all time slices, if number of times someone is leading, is same for two or more participants, then one who come first in input sequence will be the winner.

-> Ex: If participant 2 and 3 are both leading with same number, participant 2 will be the winner.

# Constraints
1 <= T <= 100

1 <= N <= 100

# Input Format
- First line contains a single integer N denoting the number of participants
- Second line contains a single integer T denoting the total time in seconds of this Marathon.
- Next N lines (for each participant) are as follows :
- We have T+1 integers separated by space.
- First T integers are as follow:
- ith integer denotes the number of steps taken by the participant at the ith second.
- T+1st integer denotes the Distance (in meters) of each step.

# Output
- Index of Marathon winner, where index starts with 1.

# Time Limit
1

# Explanation
--> Example 1

-> Input

3

8

2 2 4 3 5 2 6 2 3

3 5 7 4 3 9 3 2 2

1 2 4 2 7 5 3 2 4

-> Output

2

-> Explanation

3 (No. of candidate)

8 (Total time of Sprint (In seconds))

2 2 4 3 5 2 6 2 3 ( data for 1st candidate. First 8 integers denote number of steps per second and last integer denotes distance covered in each step i.e. 3).

3 5 7 4 3 9 3 2 2 (similarly, 2nd candidate's data).

1 2 4 2 7 5 3 2 4 (similarly, 3rd candidate's data).

At time 2: Here 2nd marathoner is leading

12 (2*3+2*3)

16 (3*2+5*2)

12 (1*4+2*4)

At time 4 :Here also 2nd marathoner is leading

33 ( 2*3+2*3 +4*3+3*3)

38

36

At time 6 :Here 3rd marathoner is leading

57

62

84

-> Output:

2

Since, 2nd marathoner is leading more number of times, so 2 is the winner.
