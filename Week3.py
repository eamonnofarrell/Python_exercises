#Code by Eamonn O'Farrell 7/2/18
#Collaz conjecture excercise
# Complete the exercise discussed in the Collatz conjecture video by writing a 
#single Python script that starts with an integer and repeatedly applies the 
#Collatz function (divide by 2 if even, multiply by three and 1 if odd) #
#using a while loop and if statement. At each iteration, the current value of 
#the integer should be printed to the screen. You can specify in your code 
#the starting value of 17. If you wish to enhance your program, 
#have the program ask the user for the integer instead of specifying a 
#value at the start of your code. Add the script to your GitHub repository,
#as per the instruction in the Assessments section.

n = int(input("Please enter an integer: "))

while n>1:
    if n%2 == 0:
       n= n/2
       print (n)
    elif n/2  > 0:
       n= (n*3) +1
       print (n)
