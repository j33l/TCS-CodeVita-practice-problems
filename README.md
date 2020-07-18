# Index

<details>
  <summary>A) A Board Game</summary>

  You are given an N x N grid of squares. Each square except the top left is filled with a positive integer. You start at the top
left corner with a score of 0 and move to the bottom right square by moving either right by one square or down by one square. As
you move to the new square, your score becomes `[S/2] + k`, where `S` was the score at your previous square and k is the number 
written in the current square. In the above, [x] is the largest integer which is not greater than x. Thus, [5] is 5, and [5.5] is 
also 5.
Write a program to find the smallest score with which you can exit the grid.
</details>

<details>
  <summary>B) Paper Generation</summary>

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
</details>

<details>
  <summary>C) New ATM Design</summary>
Automated Teller Machine (ATM) is an electronic device that enables people to withdraw cash from their bank account.
Every ATM has a limit for number of currency notes (say N), it can give at a time.

-> A bank wants to design an ATM for school students. The unique feature of this ATM would be that it would always give
maximum number of currency notes possible, to make the students happy.  Available denomination of currency notes in the ATM
are 100, 200, 500, 1000
</details>

<details>
  <summary>D) Marathon Winner</summary>

 Race is generally organized by distance but this race will be organized by time.
In order to predict the winner we will check every 2 seconds.
Let's say total race time is 7 seconds we will check for (7-1) seconds.
For 7 sec : We will check who is leading at 2 sec, 4 sec and 6 sec.
Participant who is leading more number of times is winner from prediction perspective.

-> Now our task is to predict a winner in this marathon.

-> Note:
- 1) At particular time let say at 4th second, top two (top N, in general) participants are at same distance, then in this case both are leading we will increase count for both (all N).
- 2) And after calculating at all time slices, if number of times someone is leading, is same for two or more participants, then one who come first in input sequence will be the winner.

-> Ex: If participant 2 and 3 are both leading with same number, participant 2 will be the winner.
</details>

<details>
  <summary>E) Lexi String</summary>

  - Little Jill jumbled up the order of the letters in our dictionary. Now, Jack uses this list to find the smallest lexicographical string that can be made out of this new order. Can you help him?

- (In mathematics, the lexicographic or lexicographical order is a generalization of the way words are alphabetically ordered based on the alphabetical order of their component letters.)

- You are given a string P that denotes the new order of letters in the English dictionary. 
- You need to print the smallest lexicographic string made from the given string S.
</details>

<details>
  <summary>F) Similar Char</summary>

  Tahir and Mamta are woking in a project in TCS. Tahir being a problem solver came up with an interesting problem for his friend Mamta. 

Problem consists of a string of length N and contains only small case alphabets. 

It will be followed by Q queries, in which each query will contain an integer P (1<=P<=N) denoting a position within the string. 

Mamta's task is to find the alphabet present at that location and determine the number of occurrence of same alphabet preceding the given location P.

Mamta is busy with her office work. Therefore, she asked you to help her.
</details>

* * *

<details>
  <summary>A2) Philaland Coin</summary>

  The problem solvers have found a new Island for coding and named it as Philaland.  
These smart people were given a task to make purchase of items at the Island easier by distributing various coins with different  
value.  

-> Manish has come up with a solution that if we make coins category starting from $1 till the maximum price of item present on  
Island, then we can purchase any item easily. He added following example to prove his point.  

-> Lets suppose the maximum price of an item is 5$ then we can make coins of {$1, $2, $3, $4, $5} to purchase any item ranging from  
$1 till $5.

-> Now Manisha, being a keen observer suggested that we could actually minimize the number of coins required and gave following  
distribution {$1, $2, $3}. According to him any item can be purchased one time ranging from $1 to $5. Everyone was impressed with   
both of them.  
</details>

<details>
  <summary>B2) Prime Fibonnaci
</summary>

  - Given two numbers n1 and n2
1. Find prime numbers between n1 and n2, then...
2. Make all possible unique combinations of numbers from the prime numbers list you found in step 1. 
3. From this new list, again find all prime numbers.
4. Find smallest (a) and largest (b) number from the 2nd generated list, also count of this list.
5. Consider smallest and largest number as the 1st and 2nd number to generate Fibonacci series respectively till the count (number of primes in the 2nd list).
6. Print the last number of a Fibonacci series as an output
</details>

<details>
  <summary>C2) Collision Course</summary>

- On a busy road, multiple cars are passing by. A simulation is run to see what happens if brakes fail for all cars on the road.  
- The only way for them to be safe is if they don't collide and pass by each other.  
- The goal is to identify whether any of the given cars would collide or pass by each other safely around a Roundabout. Think of this as a reference point O ( Origin with coordinates (0,0) ), but instead of going around it, cars pass through it.
- Considering that each car is moving in a straight line towards the origin with individual uniform speed. Cars will continue to travel in that same straight line even after crossing origin. Calculate the number of collisions that will happen in such a scenario.

Note : - Calculate collisions only at origin. Ignore the other collisions. Assume that each car continues on its respective path even after the collision without change of direction or speed for an infinite distance.
</details>

<details>
  <summary>D2) Television Sets</summary>

 - Dr. Vishnu is opening a new world class hospital in a small town designed to be the first preference of the patients in the city.
- Hospital has `N` rooms of two types - with TV and without TV, with daily rates of `R1` and `R2` respectively. 
- However, from his experience Dr. Vishnu knows that the number of patients is not constant throughout the year, instead it follows a pattern.
- The number of patients on any given day of the year is given by the following formula  `(6-M)^2 + |D-15|` where `M` is the number of month (1 for jan, 2 for feb ...12 for dec) and `D` is the date (1,2...31).
- All patients prefer without TV rooms as they are cheaper, but will opt for with TV rooms only if without TV rooms are not available.
- Hospital has a revenue target for the first year of operation. Given this target and the values of `N`, `R1` and `R2` you need to identify the number of TVs the hospital should buy so that it meets the revenue target.
- Assume the Hospital opens on 1st Jan and year is a non-leap year. 
</details>

<details>
  <summary>E2) Lazy Student</summary>

 - There is a test of Algorithms. Teacher provides a question bank consisting of `N` questions and guarantees all the questions in the test will be from this question bank.
- Due to lack of time and his laziness, Codu could only practice `M` questions.
- There are `T` questions in a question paper selected randomly.
- Passing criteria is solving at least `1` of the `T` problems.
- Codu can't solve the question he didn't practice. What is the **probability** that Codu will pass the test?
</details>

<details>
  <summary>F2) Lifeguard Prob</summary>

  A life guard is sitting on a beach on a lookout for potential emergencies.

He suddenly notices a person who is drowning and springs to action.

He runs up to the sea with a speed f*V km/hr, then he swims straight to the person at the rate V km/hr (both in straight lines and where f is a multiplying factor as humans run much faster than they can swim).

He wants to minimize the time taken to get to that person.
</details>

* * *

A - F m2 - mockVita-2@17-7-2020

## Have a better solution, please create a "pull request". Thanks.😃
