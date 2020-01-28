# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 17:32:53 2017

@author: FuckYouMicrosoft
"""

s = str(input('Enter a word: '))
word_length = len(s)
word_count = 0 
name = 'bob'
name_count = 0
while word_count < word_length:
    if s[word_count:word_count+3] == name:
        name_count = name_count + 1
    word_count = word_count + 1
if word_count == word_length:
    print('Number of time bob occurs is: ', name_count)
