Petrol Pump
Problem Description
A big group of students, starting a long journey on different set of vehicles need to fill petrol in their vehicles.

As group leader you are required to minimize the time they spend at the petrol pump to start the journey at the earliest. You will be given the quantity of petrol (in litres) that can be filled in each vehicle. There are two petrol vending machines at the petrol pump. You need to arrange the vehicles in such a way that they take shortest possible time to fill all the vehicles and provide the time taken in seconds as output. Machine vends petrol @ 1litre/second.

Assume that there is no time lost between switching vehicles to start filling petrol.

Constraints
1<= Number of vehicles < 50.

0 <= Quantity of petrol required in any vehicle <= 200

Input Format
First line will provide the quantity of petrol (separated by space) that can be filled in each vehicle.

Output
Shortest possible time to fill petrol in all the vehicles.

Timeout
1

Explanation
Example 1

Input

1 2 3 4 5 10 11 3 6 16

Output

31

Explanation

First Petrol vending machine will cater to vehicles taking - 16, 6, 4, 3, 2 litres of petrol (Total 31 sec)

Second machine will cater to vehicles taking - 11, 10, 5, 3, 1 litres of petrol (Total 30 sec)

Example 2

Input

25 30 35 20 90 110 45 70 80 12 30 35 85

Output

335

Explanation

First Petrol vending machine will cater to vehicles taking - 80, 45, 35, 30, 25, 12, 85, 20 litres of petrol.

Second machine will cater to vehicles taking - 90, 70, 35, 30, 110 litres of petrol. Since second machine will take more time, total time to fill petrol in all vehicles will be 335 seconds.