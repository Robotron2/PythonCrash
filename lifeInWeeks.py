# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 07:51:54 2022

@author: Theophilus
"""

assumedAge = 90
userAge = int(input("Enter your age: "))

yearsLeft = assumedAge - userAge
monthsLeft = yearsLeft * 12
weeksLeft = yearsLeft * 52
daysLeft = yearsLeft * 365

print(f"You have {yearsLeft} years left, {monthsLeft} months left, {weeksLeft} and {daysLeft} until 90 years")

