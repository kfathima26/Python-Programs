#Ask  the user for the 3 fav movies and store them in a list.
movie1=input("Enter the 1st fav movie:")
movie2=input("Enter the 2nd fav movie:")
movie3=input("Enter the 3rd fav movie:")

movieslist=[movie1, movie2, movie3]
print(movieslist)

#Create a Tuple of marks(87,64,33,95,76) and print the highest and lowest marks using max()and min()
marks=(87,64,33,95,76)
Tuple=marks
print(Tuple)
print(max(Tuple))
print(min(Tuple))
print(len(Tuple))
print(Tuple[0:3])

#Write a pgm to check grade based on marks (A/B/C/D) using if-elif-else

marks=int(input("Enter your marks:"))
if(marks>=90):
    print("Your Grade is A")
elif(marks>=85):
    print("Your Grade is B")
elif(marks>=70):
    print("Your Grade is C")
else:
    print("Your Grade is D")
    
    #OR
    marks=98
if(marks>=90):
    print("Your Grade is A")

    marks=87
elif(marks>=85):
    print("Your Grade is B")
    marks=70
else:
    (marks>=70)
    print("Your Grade is C")
    marks=64
    print("Your Grade is D")
