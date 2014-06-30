#Source: Problem 3 from Project Euler - https://projecteuler.net/problem=3
#Author: Tyson Elford
#Date: June 30, 2014

#Problem:
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

#My Solution:

#Step 1, find the factors of the large number from high to low
#Step 2, find out if that factor is prime, the first prime will be the highest

#Fields
largeNum = 600851475143

#Function test if a given number is a factor
def isFactor(num):
	global largeNume
	if(largeNum % num == 0):
		return True
	else:
		return False
		
#Function to check if a number is prime
def isPrime(num):
	for i in range(2, num - 1):
		if(num % i == 0):
			#Number is not prime
			return False
	return True
	
#Run the program to test the factors starting top down
testNumber = largeNum - 2
while(testNumber > 1):
	if(testNumber % 5 == 0): #Skip factors of 5, not prime
		testNumber -= 2
		continue;
	if(isFactor(testNumber)): #Step 1 from above
		print "Found factor: %d" % testNumber
		if(isPrime(testNumber)): #Step 2 from above
			print "The highest prime factor of %d is %d" % (largeNum, testNumber) #Highest prime factor found
			break;
	testNumber -= 2 #Skip Even numbers becuase they will not be primes