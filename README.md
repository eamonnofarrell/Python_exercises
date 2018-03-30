
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
- My name is Eamonn O Farrell. I am a student of GMIT, completing a post graduate Higher Diploma in Science in Computing (Data Analytics). 
- This GitHub repository has been created in order to store the weeky Python programming language exercises required for the Programming and Scripting module. 

## Week1 
- The information relating to the exercise for week 1 is contained in file Week1&Week2.txt. 
- The objective of the exercise is to calculate the nth Fibonacci number where n the sum of the first and last letters of your first name as numbers. 
- *In mathematics, the Fibonacci numbers are the numbers in the following integer sequence, called the Fibonacci sequence, and characterized by the fact that every number after the first two is the sum of the two preceding ones 1,1,2,3,5,8,13,21,34,55...etc* Ref Wikipedia: https://en.wikipedia.org/wiki/Fibonacci_number

```javascript
My name is Eamonn, so the first and last letter of my name (E + N = 5 + 14) give the number 19.  
The 19th Fibonacci number is 4181.
```

## Week2 
- The information for week 2 is also available file Week1&Week2.txt. 
- Student is required to change the string variable in code from tutorial to contain own surname, and rerun it. 
- Function ord() returns an integer representing the Unicode code point of that character.

```javascript
My surname is, OFarrell
The first letter O, is number 79
The last letter l, is number 108
Fibonacci number 187, is 538522340430300790495419781092981030533L
ord() returns an integer representing the Unicode code point of that character.
```

## Week3 
- The filename for week 3 exercise is Week3.py and is focused on the Collatz conjecture. 
- *The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined as follows: start with any positive integer n. Then each term is obtained from the previous term as follows: if the previous term is even, the next term is one half the previous term. Otherwise, the next term is 3 times the previous term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.* Ref Wikipedia: https://en.wikipedia.org/wiki/Collatz_conjecture. 
- Requirement for this exercise is to write a single Python script that starts with an integer and repeatedly applies the Collatz function (divide by 2 if even, multiply by three and 1 if odd) using a while loop and if statement.

```javascript
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
- This weeks exercise is in file Week4_Euler.py. 
- *Euler was a Swiss mathematician, physicist, astronomer, logician and engineer, who made important and influential discoveries in many branches of mathematics. Problem 5 from project Euler is laid out as follows. 2,520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.* 
- Student is required to write a Python program using for and range to calculate the smallest positive number that is evenly divisible by all of the numbers from 1 to 20. Add your answer to your GitHub repository.

```javascript
def gcd(a, b):
    """Calculate and return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def lcmm(*args):
    """Return lcm of args."""   
    return reduce(lcm, args)

def lcm_seq(seq):
    """Return lcm of sequence."""
    return reduce(lcm, seq)

solution = lcm_seq(xrange(1,21))
print "lcm_seq():", solution
```
## Week5 
- Week 5 Python excercise is contaned in Week5_Iris.py. 
- Student is required to write a script that reads the Iris data set in and prints the four numerical values on each row in a nice format. 

```javascript
with open("Data/iris.csv") as f:
    #print headings
    print("Petal Length Petal Width  Sepal Length Sepal Width")
    #use line split to print in columns
    for line in f:
        print(line.split(',')[0],"        ",line.split(',')[1],
        "        ",line.split(',')[2],"        ",line.split(',')[3])
```

## Week6

- Python exercise is detailed in file Week6_Factorial.py. Student is required to write a Python script containing a function called factorial(). 
- The function takes a single input/argument which is a positive integer and returns its factorial.

```javascript
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
## Table of Contents (Optional)

> If you're `README` has a lot of info, section headers might be nice.

- [Installation](#installation)
- [Features](#features)
- [Contributing](#contributing)
- [Team](#team)
- [FAQ](#faq)
- [Support](#support)
- [License](#license)


---

## Example (Optional)

```javascript
// code away!

let generateProject = project => {
  let code = [];
  for (let js = 0; js < project.length; js++) {
    code.push(js);
  }
};
```

---

## Installation

- All the `code` required to get started
- Images of what it should look like

### Clone

- Clone this repo to your local machine using `https://github.com/fvcproductions/SOMEREPO`

### Setup

- If you want more syntax highlighting, format your code like this:

> update and install this package first
