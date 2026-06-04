#Dictionaries (unordered,mutable,dont allow duplicae keys)

student={
    "name":"Kisa",
    "age":20,
    "city":"New York",
    "Roll No":28,
    }
print(type(student))
print(student["name"])
print(student["age"])
print(student["city"])
print(student["Roll No"])
student["age"]="23" #Updating the value of age key
print(student)
student["favsubject"]="Maths" #Adding new key value
print(student)
student.pop("favsubject") #Removing the key value pair
print(student)
print(student.keys()) #To get all the keys in the dictionary
print(student.items())