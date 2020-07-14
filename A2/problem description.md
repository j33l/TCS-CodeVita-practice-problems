# Philaland Coin

--> Problem Description
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

### Your task is to help Manisha come up with minimum number of denominations for any arbitrary max price in Philaland.

## Constraints
1<=T<=100

1<=N<=5000

## Input Format
First line contains an integer T denoting the number of test cases.

Next T lines contains an integer N denoting the maximum price of the item present on Philaland.

## Output
For each test case print a single line denoting the minimum number of denominations of coins required.

## Timeout
1


## Test Case
### Example 1

#### Input
2  
10  
5  

#### Output
4  
3  

#### Explanation

For test case 1, N=10.

According to Manish {$1, $2, $3,... $10} must be distributed.

But as per Manisha only {$1, $2, $3, $4} coins are enough to purchase any item ranging from $1 to $10. Hence minimum is 4. Likewise denominations could also be {$1, $2, $3, $5}. Hence answer is still 4.

For test case 2, N=5.

According to Manish {$1, $2, $3, $4, $5} must be distributed.

But as per Manisha only {$1, $2, $3} coins are enough to purchase any item ranging from $1 to $5. Hence minimum is 3. Likewise denominations could also be {$1, $2, $4}. Hence answer is still 3.
