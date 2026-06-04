#You are given alist of programming languages:
#{"Python", "Java", "C++","Python","Java","C"}
#Convert it into a set and print howmany unique languages you know.

programmingList=["Python", "Java", "C++","Python","Java","C"]
print(type(programmingList))

#covert a list into a set
programmingSet=set(programmingList)


print(type(programmingSet))
print("Languages you know",len(programmingSet))

