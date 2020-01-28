# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 12:58:11 2017

@author: FuckYouMicrosoft
"""
balance = 320000
annualInterestRate = 0.2
temp = balance
monthlyInterestRate = annualInterestRate/12
lowP = balance / 12
highP = (balance*(1+monthlyInterestRate)**12)/12.0



while abs(balance) > 0.009:
    iteration = 0
    balance = temp
    p = (lowP+highP)/2
    for iteration in range(12):
        
        balance -= p
        balance = balance + balance*(annualInterestRate/12)
    
    if balance > 0:    
        lowP = p
    elif balance < 0:
        highP = p
    else:
        break

print('Lowest Payment: '+ str(round(p, 2)))