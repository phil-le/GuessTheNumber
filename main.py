""" The Goal: Similar to the first project, this project also uses the 
random module in Python. The program will first randomly generate a number 
unknown to the user. The user needs to guess what that number is. (In other 
words, the user needs to be able to input information.) If the user’s guess 
is wrong, the program should return some sort of indication as to how wrong 
(e.g. The number is too high or too low). If the user guesses correctly, a 
positive indication should appear. You’ll need functions to check if the 
user input is an actual number, to see the difference between the inputted 
number and the randomly generated numbers, and to then compare the numbers.
"""

from random import randint
from msvcrt import getch

while(1):
    print("Welcome to Guess The Number!")
    rand_int = randint(0,100) #creates random number been 0-100
#    print (rand_int)
    while(1):
        guess_val = input("Guess the number! (0-100): ")
        guess_int = int(guess_val) #convert object to int
        if(int(guess_val) == rand_int):
            print("Correct! \nPress ENTER for new game.")
            key = ord(getch()) #single key input
            if(key != 255): #check for no key
                if (key == 13): #if enter is pressed
                    break
                else:
                    exit()
            break
        else:
            if(guess_int > rand_int):
                print("Try a lower number.")
            else:
                print("Try a higher number.")
