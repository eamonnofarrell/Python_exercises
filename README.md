
##  Table of Contents

<img  width=200 align="right" src="python.jpg">

- [Introduction](#introduction)
- [Week1](#week1)
- [Week2](#week2)
- [Week3](#week3)
- [Week4](#week4)
- [Week5](#week5)
- [Week6](#week6)

---
<img align="centre" src="GMIT.jpg">

## Introduction
- My name is Eamonn O Farrell. I am currently pursuing a post graduate Higher Diploma in Data Analytics at the Galway-Mayo Institiute of Technology.
- The purpose of this GitHub repository is to host the weeky Python programming language data analytics exercises required for the Programming and Scripting module. 
- [Python](https://www.python.org/) is an interpreted high-level programming language used for general-purpose programming.  

## Week1 
- The information relating to the exercise for week 1 is contained in file [Week1&Week2.txt](./Week1&Week2.txt)
- The objective of the exercise is to calculate the nth Fibonacci number where n the sum of the first and last letters of your first name as numbers. 
- *In mathematics, the Fibonacci numbers are the numbers in the following integer sequence, called the Fibonacci sequence, and characterized by the fact that every number after the first two is the sum of the two preceding ones 1,1,2,3,5,8,13,21,34,55...etc* Ref Wikipedia: https://en.wikipedia.org/wiki/Fibonacci_number

```javascript
My name is Eamonn, so the first and last letter of my name (E + N = 5 + 14) give the number 19.  
The 19th Fibonacci number is 4181.
```

## Week2 
- The information for week 2 is also available in file [Week1&Week2.txt](./Week1&Week2.txt)
- Student is required to change the string variable in code from tutorial to contain own surname, and rerun it. 
- Function ord() returns an integer representing the Unicode code point of that character.

```
My surname is, OFarrell
The first letter O, is number 79
The last letter l, is number 108
Fibonacci number 187, is 538522340430300790495419781092981030533L
ord() returns an integer representing the Unicode code point of that character.
```

## Week3 
- The filename for week 3 exercise is [Week3.py](./Week3.py) and is focused on the Collatz conjecture. 
- *The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined as follows: start with any positive integer n. Then each term is obtained from the previous term as follows: if the previous term is even, the next term is one half the previous term. Otherwise, the next term is 3 times the previous term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.* Ref Wikipedia: https://en.wikipedia.org/wiki/Collatz_conjecture. 
- Requirement for this exercise is to write a single Python script that starts with an integer and repeatedly applies the Collatz function (divide by 2 if even, multiply by three and 1 if odd) using a while loop and if statement.

```
#prompt user to input number
n = int(input("Please enter an integer: "))
#use while loop to ensure coe runs as long as number is greater than 1
while n>1:
    #check if remainder is 0
    if n%2 == 0:
       n= n/2
       print (n)
     #use else if to establish if result is bigger than 0 when divided by 2
    elif n/2  > 0:
       n= (n*3) +1
       print (n)
```

## Week4 
- This weeks exercise is saved in file [Final_Eul5.py](./Final_Eul5.py)
- *Euler was a Swiss mathematician, physicist, astronomer, logician and engineer, who made important and influential discoveries in many branches of mathematics. Problem 5 from project Euler is laid out as follows. 2,520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.*  Ref Wikipedi: https://en.wikipedia.org/wiki/Leonhard_Euler
- Student is required to write a Python program using for and range to calculate the smallest positive number that is evenly divisible by all of the numbers from 1 to 20. 
- Euclid's Algorithm is used in the solution to find the smallest multiple
- *The Euclidean algorithm is based on the principle that the greatest common divisor of two numbers does not change if the larger number is replaced by its difference with the smaller number. For example, 21 is the GCD of 252 and 105 (as 252 = 21 × 12 and 105 = 21 × 5), and the same number 21 is also the GCD of 105 and 252 − 105 = 147. Since this replacement reduces the larger of the two numbers, repeating this process gives successively smaller pairs of numbers until the two numbers become equal. When that occurs, they are the GCD of the original two numbers.* Ref Wikipedia: https://en.wikipedia.org/wiki/Euclidean_algorithm 

```#Define function gcd
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
```
## Week5 
- Week 5 Python excercise is contaned in [Week5_Iris.py](./Week5_Iris.py).
- Student is required to write a script that reads the Iris data set in and prints the four numerical values on each row in a nice format. 
- *The Iris Data Set is a small dataset from 1936 introduced by the British statistician and biologist Ronald Fisher. It is often used for testing machine learning algorithms and visualizations (for example, Scatter Plot). Each row of the table represents an iris flower, including its species and dimensions of its botanical parts, sepal and petal, in centimeters.* Ref Wikipedia
- The solution uses method line.split() to return a list of all the words in the string. 

```
with open("Data/iris.csv") as f:
    #print headings
    print("Petal Length Petal Width  Sepal Length Sepal Width")
    #use line split to print in columns
    for line in f:
        print(line.split(',')[0],"        ",line.split(',')[1],
        "        ",line.split(',')[2],"        ",line.split(',')[3])
```

## Week6

- Python week 6 exercise is detailed in file [Week6_Factorial.py](./Week6_Factorial.py). Student is required to write a Python script containing a function called factorial(). 
- The function takes a single input/argument which is a positive integer and returns its factorial.
- In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example, 5! = 5 x 4 x 3 x 2 x 1 = 120.
- Solution is to define a function factorial() that takes an integer p and multiplies p by p - 1 until p equals 0.

```
#define function factorial and process with argument p
def factorial(p):
    #check if parameter passed equals 1. If so return value 1
    if  p== 0:
        return 1
    #otherwise, multiply p by p minus 1 until equal to 0 
    else:
        return p * factorial(p-1)

#set parameter p, call function factorial and print result
p=5
print (factorial(p))
```
