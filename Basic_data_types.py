#python key concepts


#*******************************
"""
#data types
#lists, tuples, dictionaries

#operators (-,+,/,*,%)

#adding strings (concatenation)

MyName = "Bryan"
FirstName = "Bryan"
secondName = "Muchai"
fullName = FirstName + " " + secondName
print(fullName)

#slice string function
random = "dkndsoivsdiBryandcdnef"
print(random[3:10])
"""


#**********************************

#list/Arrays
"""
shoppingList = "eggs, milk, butter, sausages"
#this prints the whole list as a single string
 #using a list/Array
shoppingList2 = ["eggs", "milk", "butter", "sausages"]

#arrays help us use indexing to get our values
print(shoppingList2[2])

#updating a list
shoppingList2[1] = "yoghurt"
print(shoppingList2)


#deleting from a list
del shoppingList2[3]
print(shoppingList2)

#use append function to add an object to a list
shoppingList2.append("Kale")
print(shoppingList2)
#count number of times something is repeating
shoppingList2.count("eggs")

#adding Arrays together
array1= [34, 23, 56, 40]
array2= [45, 3, 23, 56]
array3 = array1 + array2
print(array3)

#getting length of array: use the len function
arrayLength = len(array3)
print(arrayLength)

#gettig max or min from an array
max1= max(array3)
min1= min(array3)
print(max1)
"""
#**************************************************

#dictionaries
"""
#they work just like map legends: comes with a key and a value
#suppose you have a class of 10 students.
students = {"Erick":14, "Bob":12, "Tina":15}

#updating dictionary
students["Bob"] = 13
del students["Tina"]
#functions used in dictionaries

students.clear() #prints an empty list


del students  #completely removes the dictionary

students = {"Jobs":21,"Marco":23,"Avril":20,"Lena":22}
len1 = len(students) #prints number of Key/value items in a disctionary
print(len1)
#if you want to print keys only (notice the values are pritned randomly: no indexing)
print(students.keys())
print(students.values())

students2 = {"Levi":24, "Kip":20,"Vee":24}
#use the update function to add values of a dictionary to another

students.update(students2)
print(students)
"""

#**********************************************************

#tuples

#tuples are similar to lists but the data in tuples cannot change(immutable)
tup1 = ("Maths",23, "Dogs")
#tup1.append("elt") prints attribute error


#slicing in tuples
print(tup1[0]) #prints maths
print(tup1[0:2]) #prints 'Maths', 23


