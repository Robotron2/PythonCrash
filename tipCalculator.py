# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 08:10:01 2022

@author: Theophilus
"""



initialBill = int(input("Enter your bill here: $"))
askPercentage = int(input("Enter the percentage you would want to give as tip: 10%, 12%, 15% : "))
askNumberOfPeople = int(input("How many people are meant to share this bill? "))

calculateBill = initialBill * (askPercentage/100)
tipPerPerson = calculateBill / askNumberOfPeople
roundTipPerPerson = round(tipPerPerson, 2)

print(f"Each person would pay ${roundTipPerPerson}")
