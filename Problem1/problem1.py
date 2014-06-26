#Source: Problem 1 from Project Euler - https://projecteuler.net/problem=1
#Author: Tyson Elford
#Date: June 26, 2014

#Problem:
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

#My Solution:

#Function to test if a value is a multiple of 3
def isMultipleOf3(num):
	if(num % 3 == 0):
		return True
	else:
		return False
	
#Function to test if a value is a multiple of 5	
def isMultipleOf5(num):
	if(num % 5 == 0):
		return True
	else:
		return False

#Run the program, starting at 1 and finishing at 999
#Make sure to add to the total
total = 0
for i in range(1, 1000):
	if(isMultipleOf3(i)):
		total += i
	if(isMultipleOf5(i)):
		total += i
		
print total
#Total should be 266,333

