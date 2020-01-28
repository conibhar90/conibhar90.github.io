# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 21:32:14 2017

@author: FuckYouMicrosoft
"""

def applyF_filterG(L, f, g):
    temp = []
    temp = L
    L2 = temp
    temp = []
   
    for i in L:
        if g(f(i)) == False:
            L2.remove(i)
    
    if L2 == []:
        return -1
    
    else:
        print(L)
        print(L2)
        return max(L2)
    
    
    
def f(i):
    return i + 2

def g(i):
    return i > 5

