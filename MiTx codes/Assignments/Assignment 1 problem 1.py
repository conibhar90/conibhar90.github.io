# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 17:32:53 2017

@author: FuckYouMicrosoft
"""

s = str(input('Enter a word: '))
word_length = len(s)
word_count = 0 
vowels = 'aeiou'
vowels_count = 0
while word_count < word_length:
    if s[word_count] in vowels:
        vowels_count = vowels_count + 1
    word_count = word_count + 1
if word_count == word_length:
    print('Number of vowels: ', vowels_count)