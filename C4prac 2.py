#Write a pgm that takes a names of 3 fav foods from the user and stores them in a list.Then print the list and its length.
food=input("Enter the 3 fav foods:")
foodlist=food.split(",")
print(foodlist)
print(len(foodlist))

#OR
food1=input("Enter the 1st fav food:")
food2=input("Enter the 2nd fav food:")
food3=input("Enter the 3rd fav food:")
foodlist=[food1,food2,food3]

foodlist.append(food1)
foodlist.append(food2)
foodlist.append(food3)
print(foodlist)

#Strings are immutable
#Tuples are immutable
#Lists are mutable (change can be done)

myTuple=(60,70,80)
studentTuple=("Kisa","Riya","Sia")
print(len(myTuple))


print(studentTuple)
print(myTuple)
print(studentTuple[0])

#Empty Tuples-Interview qn
emptyTuple=()
singleTuple=(1,)
print(type(emptyTuple))
print(type(studentTuple))
print(type(singleTuple))
print(studentTuple.index("Riya"))
print(studentTuple.count("Kisa"))

#Create a tuple of ur fav 5 fruits then print
#The total number of fruits
#The index of one selected fruit

fruits=("Mango","Grapes","Strawberry","Apple","Banana")
print(len(fruits))
print(fruits.index("Strawberry"))


