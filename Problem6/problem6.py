#Source: Problem 6 from Project Euler - https://projecteuler.net/problem=6
#Author: Tyson Elford
#Date: July 7, 2014

#Problem:
#The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385
#The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

#My Solution:

#Fields
sumOfSquares = 0
squareOfSum = 0

#Find the sum of squares and the sum to be squared
for i in range(0, 101):
	sumOfSquares += i ** 2
	squareOfSum += i
	
#Square the second sum
squareOfSum = squareOfSum ** 2

#Find the difference and print the answer
print "The difference is %d" % (squareOfSum - sumOfSquares)
	