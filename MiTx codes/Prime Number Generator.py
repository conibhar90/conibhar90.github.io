# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 22:20:31 2017

@author: FuckYouMicrosoft
"""

def genPrimes():
    
    list_primes = []   
    last_prime = 1      
    
    while True:
        last_prime += 1
        for primes in list_primes:
            if last_prime % primes == 0:
                break
        else:
            list_primes.append(last_prime)
            yield last_prime
    