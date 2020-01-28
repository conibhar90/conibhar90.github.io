# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 23:08:36 2017

@author: FuckYouMicrosoft
"""


def flatten(aList):
    neatList = []
    for i in aList:
        if type(i) == list:
            neatList += flatten(i)
        else:
            neatList.append(i)
    
    return neatList
    