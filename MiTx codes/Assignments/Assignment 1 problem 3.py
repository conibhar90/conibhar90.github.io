# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 18:15:14 2017

@author: FuckYouMicrosoft
"""

s = str(input('Enter a word: '))
word_length = len(s)
word_count = 1
temp_word = s[0]
substring = s[0] 


while word_count < word_length:
    if s[word_count] >= s[word_count-1]:
        temp_word += s[word_count]
        if len(temp_word) > len(substring):
            substring = temp_word
    else: 
        temp_word = s[word_count]
    word_count += 1
    
print("Longest substring in alphabetical order is: " + substring)
        
    