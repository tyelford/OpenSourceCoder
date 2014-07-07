#Source: Problem 5 from Project Euler - https://projecteuler.net/problem=5
#Author: Tyson Elford
#Date: July 7, 2014

#Problem:
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


#My Solution:

#Function to check if a given number is the solution
def checkNum (num):
	for i in range(1, 21):
		if(isEvenly(num, i)):
			continue
		else:
			return False
	#If the loop finishes than we have a solution
	return True
	
	
#Function to check if a number is evenly divisible
def isEvenly (num, div):
	if(num % div == 0):
		return True
	else:
		return False
		
#Run the program
checkThisNum = 1
while(True):
	if(checkNum(checkThisNum)):
		print "We found the solution: %d" % checkThisNum
		break
	checkThisNum += 1