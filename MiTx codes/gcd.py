# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 00:50:11 2017

@author: FuckYouMicrosoft
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    
    if a == 0:
        return b
    
    elif b == 0:
        return a
    
    elif a > b:
        return gcdRecur(b, a%b)
    
    else:
        return gcdRecur(a, b%a)
        