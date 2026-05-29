#Assgn : pgm that takes two no and prints
#their sum,diff,and product
#Whether the first number is greater than the second

x=50
y=40
print(x+y)
print(x-y)
print(x*y)
print(x>y and x<y)
print(x>y or x<y)
print(x>=y)

#Smart Temperature Converter
#Take input in Celsius and print its Equivalent in Fahrenheit and Kelvin.
#(Use explicit type conversion and arithematic operators)

Celsius =float(input("Enter temperature in Celsius:"))
Fahrenheit = float(Celsius * 9/5)+32
Kelvin= float(Celsius+273.15)
print("Fahrenheit:",Fahrenheit)
print("Kelvin:",Kelvin)

#Bill Split Calculator
#Write a pgm that takes total bill amount and Number of friends as input
#Calculate how much each person willpay.
# Also print the data type of each variable used.
#Hint : Use float() and division operator

Total  =float(input("Total:"))
Friends=float(input("Friends:"))
Pay=(Total/Friends)
print ("Total:",Total)
print("Friends:", Friends)
print(" Pay:", Pay)
print(type(Total))
print(type(Friends))
print(type(Pay))


x=5
y=2.0
print(x//y)
print(x**y)