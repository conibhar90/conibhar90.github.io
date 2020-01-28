# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 19:44:11 2017

@author: FuckYouMicrosoft
"""

def deep_reverse(L):
    L.reverse()
    for i in L:
        i.reverse()
    return L
        