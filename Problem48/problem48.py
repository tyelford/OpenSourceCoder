#Source: Problem 48 from Project Euler - https://projecteuler.net/problem=48
#Author: Tyson Elford
#Date: June 27, 2014

#Problem:
#The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
#Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

#My Solution

totalSum = 0

for i in range (1,1001):
	totalSum += (i ** i)
	
totalSumString = str(totalSum)
print "The last ten digits are %s" % (totalSumString[-10:])