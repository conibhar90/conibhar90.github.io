# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 10:56:02 2017

@author: FuckYouMicrosoft
"""

high = 100
low = 0
ans = (high+low)//2
print('Please think of a number between 0 and 100')
print('Is your secret number '+ str(ans)+'?')
userInput = str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))
while userInput != 'c':
    if userInput == 'l' :
        low = ans
    elif userInput == 'h' :
        high =ans
    else:
        print('incorrect guess. please re-enter your guess')
    ans = (high+low)//2
    print('Is your secret number '+ str(ans)+'?')
    userInput = str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))
if userInput == 'c' :
    print('Game over. Your secret number was: ' + str(ans))