# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 12:58:11 2017

@author: FuckYouMicrosoft
"""
annualInterestRate = 0.2
p = 10
balance = 4773
temp = balance

while balance > 0:
    iteration = 0
    balance = temp
    for iteration in range(12):
        
        balance -= p
        balance = balance + balance*(annualInterestRate/12)
    
    if balance > 0:    
        p += 10
    else:
        break

print('Lowest Payment: ' + str(p))