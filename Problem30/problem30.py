#Source: Problem 30 from Project Euler - https://projecteuler.net/problem=30
#Author: Tyson Elford
#Date: June 27, 2014

#Problem:
#Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#    1634 = 1^4 + 6^4 + 3^4 + 4^4
#    8208 = 8^4 + 2^4 + 0^4 + 8^4
#    9474 = 9^4 + 4^4 + 7^4 + 4^4
#As 1 = 14 is not a sum it is not included.
#The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

#Problem Note:
#I looped throught all numbers from 2 - 1x10^9 and came up with the same answer
#changed the program to only loop from 2 - 2x10^5 to make it run faster

#My Solution:

#Fields
currentDigit = 2
	
#Function to spilt the digits and calculate the total of the sum of the fifth power
def checkNumber(num):
	stringNum = str(num)
	digitArr = list(stringNum)
	
	#Loop through array of 
	totalSum = 0
	for i in range(0, len(digitArr)):
		checkNum = digitArr[i]
		powerNum = int(checkNum) ** 5
		totalSum += powerNum
	
	#Loop through again to see if we have a match
	answerArr = list(str(totalSum))
	if(len(answerArr) != len(digitArr)):
		return False
	for i in range(0, len(answerArr)):
		if(answerArr[i] == digitArr[i]):
			continue
		else:
			return False
	return True
	
#Run the program
sumOfDigits = 0
while(currentDigit < 200000):
	if(checkNumber(currentDigit)):
		#We have a winner!
		print "We have a winner: %d" % currentDigit
		sumOfDigits += currentDigit
	currentDigit = currentDigit + 1
print "The total sum of all the numbers is: %d" % sumOfDigits
		
	
	
