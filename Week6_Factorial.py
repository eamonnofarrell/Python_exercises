#Eamonn O'Farrell

#Write a Python script containing a function called factorial() 
#that takes a single input/argument which is a positive integer 
#and returns its factorial. The factorial of a number is that 
#number multiplied by all of the positive numbers less than it. 
#For example, the factorial of 5 is 5x4x3x2x1 which equals 120. 
#You should, in your script, test the function by calling it 
#with the values 5, 7, and 10.

#define function factorial with parameter p
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
#set parameter p, call function factorial and print result
p=7
print (factorial(p))
#set parameter p, call function factorial and print result
p=10
print (factorial(p))

