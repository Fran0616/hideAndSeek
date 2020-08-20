#this code will count up from 1 to n n being any number that a user input
#the time module allows program to handle various operations reguarding timem it's conversions and representation, which finds its use in various applications in life. 
import time
#user input variable will hold the number that the user want to count up too. 
userInput = int(input("This program will count up to a number. Input the number you want to count too: "))
#the variable n will add the user input by 1 
n = userInput + 1
# the for loop will count from 1 to whatever range the user input
for i in range(1,n):
    
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    print(i, "Mississippi")
    #the python time method sleep() suspends execution for the given number of second, in this case it's 1 second
    time.sleep(1)
#Finally the program will display the message below after the count up is done. 
print ("Ready or not, here I come!")
