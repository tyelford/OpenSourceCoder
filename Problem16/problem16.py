#Source: Problem 16 from Project Euler - https://projecteuler.net/problem=16
#Author: Tyson Elford
#Date: June 27, 2014

#Problem:
#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2^1000?

#My Solution:

#Find the big number
num = 2 ** 1000

#Convert the big number into an array of chars
numArr = list(str(num))

#Loop through array and find the sum of the digits
totalSum = 0
for i in range(0, len(numArr)):
	totalSum += int(numArr[i])

print "The sum of the digits of 2^1000 is %d" % totalSum
