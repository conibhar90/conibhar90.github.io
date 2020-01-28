# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 22:30:23 2017

@author: FuckYouMicrosoft
"""
def applyF_filterG(L, f, g):

    L2 = []
    for i in L:
        if g(f(i)) == True:
            L2.append(i)
    
    L[:] = L2
    
    if L == []:
        return -1
    
    else:
        return max(L)

def f(i):
    return i + 2
def g(i):
    return i > 5

        