// reference: https://www.geeksforgeeks.org/find-number-currency-notes-sum-upto-given-amount/
// C++ program to accept an amount 
// and count number of notes 
#include <bits/stdc++.h> 
using namespace std; 

// function to count and 
// print currency notes 
void countCurrency(int amount) 
{ 
	int notes[9] = { 2000, 500, 200, 100, 
					50, 20, 10, 5, 1 }; 
	int noteCounter[9] = { 0 }; 
	
	// count notes using Greedy approach 
	for (int i = 0; i < 9; i++) { 
		if (amount >= notes[i]) { 
			noteCounter[i] = amount / notes[i]; 
			amount = amount - noteCounter[i] * notes[i]; 
		} 
	} 
	
	// Print notes 
	cout << "Currency Count ->" << endl; 
	for (int i = 0; i < 9; i++) { 
		if (noteCounter[i] != 0) { 
			cout << notes[i] << " : "
				<< noteCounter[i] << endl; 
		} 
	} 
} 

// Driver function 
int main() 
{ 
	int amount = 868; 
	countCurrency(amount); 
	return 0; 
} 
