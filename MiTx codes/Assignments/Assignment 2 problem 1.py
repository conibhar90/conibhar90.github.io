# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 11:55:31 2017

@author: FuckYouMicrosoft
"""

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
i = 0

while i < 12:
    p = balance * monthlyPaymentRate
    balance -= p
    balance = balance + balance*(annualInterestRate/12)
    i += 1
    
print('Remaining balance: '+ str(round(balance, 2)))
    