str1='Hello'
str2="Kisa"
str3='''Yes  I am Learning'''

print(str1)
print(str2)
print(str3)

#String Concatenation +
print(str1 +" " +str2) 

#Length of string
print(len(str2))

str ="Biryani"
print(str[4])

#Practice
#Write a Pythonprogram that takes a user's name as input and prints:
#1.First character
#2.The Last Character
#3.The total lenght of the name

str1="Kisa Fathima"
length =len(str1)

print(str1[0])
print(str1[10])
print(length)

#Strings are immuatable means cant change anything

#Slicing part of a string
#Syntax = string[start : end ]

str ="GulabJamun"
FirstHalf=str[0:5]
trialFirstHalf=str[:5]
print(FirstHalf)
print(trialFirstHalf)

secondHalf=str[5:10]
trialsecondHalf=str[5:]
print(secondHalf)
print(trialsecondHalf)

#Negative indexing
str ="GulabJamun"
print(str[-5:-1])
print(str[-10:-1])
print(str[-10:-5])
print(str[-7:-3])
print(str[-7:-5])

#Practice 
#Write apgm taht takes ur fav food name as input and prints
# The middle 3 characters
#The last 2 chracters
food = "Chitranna"
print(food[3:6])
print(food[7:10])


#Practice 
#Write apgm taht takes ur fav food name as input and prints
# The middle 3 characters
#The last 2 chracters
str =input("Enter the value:")
mid=len(str)//2
output1=str[mid-1:mid+2]
print(output1)
output2=str[-2:]
print(output2)

#Practice 
#Write apgm taht takes ur fav food name as input and prints
# The middle 3 characters
#The last 2 chracters
str="GREEN"
print(str[1:4])
print(str[3:5])


#String methods

str="Kisa fathima"
print(str.upper())
print(str.lower())
print(str.title())
print(str.find("hi"))
print(str.replace("fathima","Sakina"))
print(str.count("a")) #find the occurance


#Practice
#Write a pgm that
#Takes a sentence as input
#Converts it to lowercase
#Replace all spaces "" with Underscores"_"
#Prints the new string

str = "Kisa is a Developer"
print(str.lower())
print(str.replace(" ","_"))
print(str)

#Formatted String (includes variable in the string)
Name = "Kisa Fathima"
age =20
#print(f"My name is {Name}and I am {age} years old.")

#escape sequence
print("Hello World")
print("Hello\nWorld")
print("Hello \t World")