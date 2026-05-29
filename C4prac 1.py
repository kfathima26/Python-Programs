#Write a Python pgm that takes a number as inputs and prints
#  #"Positive" if no >0
#"Zero" if no == 0 
#"Negative" if no <0
num=int(input("Enter a number:"))
if(num>0):
    print("Positive")
elif(num==0):
    print("Zero")
else:
    print("Negative")

#Lists in Python 
food=["Biryani","Pizza","Burger","Mango"]
print(len(food))
print(food[0])
print(food[0:5])

#Methods in List

#indexing
#LISTS ARE MUTABLE
marks=[99,100,90,95]
print (marks)
marks[1]=98
print(marks)

#Slicing
print(marks[1:3])
print(max(marks))
print(min(marks))
marks.append(93)
print(marks)
print(marks.sort())
print(marks)
marks.pop(2)
print(marks)
marks.remove(93)
print(marks)
marks.insert(1,97)
print(marks)


#STRINGS ARE IMMUTABLE
#name="Python"
#name[0]="J"
#print(name)


