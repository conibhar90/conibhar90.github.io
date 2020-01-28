# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def closest_power(base, num):
   
    maxExponent = 0
    
    if base**maxExponent == num:
        return maxExponent
    
    else:
        
        while base**maxExponent < num:
            maxExponent += 1
        
        if base**maxExponent == num:
            return maxExponent
        
        else:
            minExponent = maxExponent - 1
            minExponentDifference = abs(num - base**minExponent)
            maxExponentDifference = abs(base**maxExponent - num)
            if minExponentDifference < maxExponentDifference:
                return minExponent
            elif maxExponentDifference < minExponentDifference:
                return maxExponent
            else:
                return minExponent
            
                
               
               
             
           
            
            
            
        