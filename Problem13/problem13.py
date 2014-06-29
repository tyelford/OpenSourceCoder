#Source: Problem 13 from Project Euler - https://projecteuler.net/problem=13
#Author: Tyson Elford
#Date: June 30, 2014

#Problem:
#Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
#See web page for the number

#My Solution:

#Read the number in from numbers.txt file and add them up
numbers = [line.strip() for line in open('numbers.txt')]

numTotal = 0
for i in range (0, len(numbers)):
	numTotal += int(numbers[i])

strNumTotal = str(numTotal)
firstTenDigits = strNumTotal[:10]
print "The first ten digits of the number are %s" % firstTenDigits
