#Source: Problem 7 from Project Euler - https://projecteuler.net/problem=7
#Author: Tyson Elford
#Date: June 27, 2014

#Problem:
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

#My Solution:

#Fields
checkPrime = 2
totalPrimes = 0
numToFind = 10001

#Function to check for a prime number
def findPrime(num):
	for i in range(2, num - 1):
		if(num%i == 0):
			#Number is not prime
			return False
	return True

#Run the main loop, break once the total number of primes needes is found
while(True):
	if(findPrime(checkPrime)):
		print "%d is a prime" % checkPrime
		totalPrimes += 1
	checkPrime += 1
	#Break when total is found
	if(totalPrimes == numToFind):
		break
print "The total number of Primes is %d" % totalPrimes
print "The %d prime number is %d" % (numToFind, checkPrime - 1)
	
