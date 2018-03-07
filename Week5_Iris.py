#Eamonn O'Farrell
#Week 5 exercise - . Write a Python script that reads the Iris data set in 
# and prints the four numerical values on each row in a nice format. 
# That is, on the screen should be printed the petal length, petal width, sepal length and sepal width,
# and these values should have the decimal places aligned, with a space between the columns.
#print(line.split(',')[0], end='')
#titles = ['petal length', 'petal width', 'sepal length', 'sepal width']

with open("Data/iris.csv") as f:
    print("Petal Length Petal Width  Sepal Length Sepal Width")
    
    for line in f:
        print(line.split(',')[0],"        ",line.split(',')[1],
        "        ",line.split(',')[2],"        ",line.split(',')[3])

