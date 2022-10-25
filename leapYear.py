# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 08:33:48 2022

@author: Theophilus
"""

year = int(input("Enter any year: "))


if (year % 4 == 0):
    
    if (year % 100 == 0 and year % 400 == 0 ):
    
        print("Leap year")
    else:
        print("Not leap year")
else:
    print("Not leap year")