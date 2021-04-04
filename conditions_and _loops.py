#conditions
"""
#if and else

if 5>2:
    print("THe world works nomally")
else:
    print("the earth has collapsed")

if 2>5:
    print("tupige sherehe")
else:
    print("better get out of this rock while we still can")


#relational operators #everytime you use a relational operator you get a boolean value back (true/d
#they include: >, <, <=, >=, ==, !=)
#if 5=5:
#   print("exes for Ys") #prints syntax error : use  double equal sign

if 5==5:
    print("hey Ninjas")
    
if 4!=6:
    print("done")


#nested if statements

name = "Bob"
age = 23
if age > 13:
    if name == "Bob":
        print("you get special priviledges")
    else:
        print("you are eligible for facebook")
    

#elif statements
day = "Tuesday"
if day == "Monday":
    print("sunny")
elif day == "Tuesday":
    print("cloudy!")
else:
    print("rainy")


#logical operators (and, or, 
#what if you want to check for more than one condition in my if statement?
age = 14
name = "Bob"
if age > 13 and name == "Avi":
    print("elligible")
#above statement doesnt return anything since both conditions arent met
    
if age > 13 or name == "Avi":
    print("elligible")  #return elligible since one of the conditions is met
"""

#***************************************************

#Loops
"""
#two type: for loops & while loops
#For loop: executes a sequence of statements multiple times and abbreviates the
    #code that manages to loop the variable

for i in range(0,5):
    print(i)
    
players = ["Messi", "Ronaldo", "Rooney","Kaka"]
for i in players:
    print(i)

tup = (2,54,67)
for i in tup:
    print(i)
    
#adding increment factor to a for loop
#for example if you wanted all even numbers
#for i in range(0,5,2):
 #   print(i)

#while loops
#repeatedly checks for one condition: if the conditon is true the code runs
    #if the condtion is false the code ends
counter = 5
while counter < 10:
    print(counter)
    counter = counter+1

#nested loop
for i in range(0,5):
    for a in range(0,5):
        print(a)

#prime number generator
for i in range(2,30):
    j = 2
    counter = 0
    while j <i: #makes sure the dividing number is not equal to i
        if i % j == 0: #checks if a number can be divided by another. if it does it skips the number and goes to the next
            counter = 1
            j = j + 1
        else:
            j = j + 1
    if counter == 0:
        print(str(i) + " is a prime number")
    else:
        counter == 0


#loop control statements: break, pass, continue
#break - breaks out of a loop
counter = 0
while counter < 100:
    if counter == 4:
        break
    print (counter)
    counter = counter + 1
    
#pass - filler statement
counter = 0
while counter < 100:
    if counter == 4:
        break
    else:
        pass
    print (counter)
    counter = counter + 1

#continue - bypasses the code you dont want to run
for i in "genghis":
    if i == "h":
        continue
    print(i)

for i in range(0,5):
    if i<2:
        continue
    print(i)



#try and except
#incase something goes wrong in the program it goes directly to the user and tell
#them something went wrong

try:
    if name > 3:
        print("Hi")
except:
    print("python ran into an error. please take a look at your code again.")



#multiline statemements
iwanttogetovermysleeping = "ew"
isthereareversesleepingpilloption = "nah"
if iwanttogetovermysleeping\
==\
isthereareversesleepingpilloption:
    print("bring it on")
else:
    print("dude you are efd")

"""

