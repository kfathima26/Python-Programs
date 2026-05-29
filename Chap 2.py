# datatypes
food="Biryani" 
age=25
area=378.3
name="Kisa"
print("Data type of Variable  name is" ,type(age))
print(type(name))
print(type(area))

# practice pgm to take age as input and print value entered and its Data type
age = input("Enter the age :")
month = 3
print("The Current Age is",age)
print( "Data type is:", type(age))
print(type(month))

# keyword = Reserved words where we cant use as normally as variablly
# Ex= and , for, if ,while,if else,try.......

# Input 2 no's and sum

input1=int(input("Enter first no :"))
input2=int(input("Enter second no :"))
sum=(input1)+(input2)
avg = ((input1)+(input2))/2
print("Sum of Two numbers is",sum)
print("Avg of Two Numbers is",avg)

#Type conversion Implicit (Automatic) it works on larger values
x=7
y=4.5
z=x+y
print(z)
print(type(z))

#Explicit (Manual)

x="10"
y=int(x)
print(y+5)

#Practice Take number as input convert into float & print both the original & converted values with their Data types
num = input("Enter a value:")
ConvertedValue = float(num)
print("The Original Value is",num,type(num))
print("The Converted Value is",ConvertedValue,type(ConvertedValue))

#Operators
x=5
y=15
print(x+y)
print(x*y)
print(x-y)
print(x/y)
print(x%y)
print(x**y)

#comparison

print(x==y)#false
print(x>y)#false
print(x<y) #true

#logical

print( "AND Operator result",x>y and x<y) #false ,both to be true
print("OR Operator result",x>y or x<y) #true , one to be true
print("Not Operator result",not(x<y)) # reverse the true into false & false into true

#Assgn operator

a=2
b=3

a=a+6
a+=6

a=a-1
a-=1

a=a/10
a/=10

a=a*10
a*=10

