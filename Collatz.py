#Code by Eamonn O'Farrell 7/2/18
#Collaz conjecture excercise

n = int(input("Please enter an integer: "))
n=17

while n>1:
    if n%2 == 0:
       n= n/2
       print (n)
    elif n/2  > 0:
       n= (n*3) +1
       print n
