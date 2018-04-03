#Eamonn O'Farrell
#Euler problem 5
#2520 is the smallest number that can be divided by 
#each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is 
#evenly divisible by all of the numbers from 1 to 20?

#ref https://gist.github.com/Anivarth/da7ceb6b0692bc3d40e0964f5175abd6
#Use euclid Algorithm to find the smallest multiple
#In mathematics, the greatest common divisor (gcd) 
# of two or more integers, which are not all zero, 
# is the largest positive integer that divides each of the integers. 
# For example, the gcd of 8 and 12 is 4.

#Define function gcd
def gcd(n1,n2):
	remainder = 1
	while remainder != 0:
		remainder = n1%n2
		n1 = n2
		n2 = remainder
	return n1

#lcm of two numbers using euclid Algorithm
#lcm = (number1*number2)/GCD(number1,number2)
def lcm(n1,n2):
	return (n1*n2)/gcd(n1,n2)

#lcm of 2,3
#You can also use (2*3)/gcd(2,3)
l = lcm(2,3)
#lcm of three numbers n1,n2,n3 is
#lcm(lcm(n1,n2),n3)
for i in range(4,21):
	l = lcm(l,i)

#Print lcm
print (l)