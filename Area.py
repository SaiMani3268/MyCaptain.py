#AREA OF CIRCLE
radius = float(input('Enter radius of the circle: '))
pie=3.1452
area=pie*radius*radius
print("The area of circle = ",area)

#OUTPUT:
Enter radius of the circle: 10
The area of circle =  314.52

#Extention 
fun_name = input("Enter the filename:")
x = fun_name.split(".")
print("The extention of the file is:" + x[-1])

#OUTPUT-1:
#Enter the filename:area.py
#The extention of the file is: py

#OUTPUT-2:
#Enter the filename:area.java
#The extention of the file is: java
