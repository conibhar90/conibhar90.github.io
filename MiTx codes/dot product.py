# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:02:01 2017

@author: FuckYouMicrosoft
"""

def dotProduct(listA, listB):
    if len(listA) == len(listB):
        listC = []
        for i in range(len(listA)):
            listC.append(listA[i]*listB[i])
        return sum(listC)