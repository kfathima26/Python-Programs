print("Line 1")
print("Line 2")
print("Line 3")

# Use id() check memory locations
x=15
print(id(x))

# Variable store references in memory
name = "Kisa Fathima"
age1 = 20
age2 = 30
print("Actual Value:",age2)
favSubject ="Python"
age2=age1
print("Changed Value:" ,age2)

# Program to take input from the user
# Use input() to get user input
# input() always returns a String

print("A sample program to Understand input method in python")

name= input("Enter yor good name :")
age= input("Enter your age :")
print ("Your good name is:",name)
print ("Your current age is:",age)

#Assgn Que
# Take diameter as input and calculate the area of a circle
diameter =int(input("Enter the value of diameter:"))
radius = diameter/2
area = 3.14 *(radius**2)
print("Radius of the circle is",radius)
print("Area of the circle is",area)


