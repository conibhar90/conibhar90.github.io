# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 13:12:08 2017

@author: FuckYouMicrosoft
"""
count = 0
phrase = "hello, world"
for iteration in range(5):
    while True:
        count += len(phrase)
        break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
