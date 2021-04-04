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
