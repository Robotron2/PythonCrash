# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 08:57:37 2022

@author: Theophilus
"""

print("Welcome to Python Pizza Deliveries!!")
size = input("What size do you want? S, M, L: ")
addPepperoni = input("Do you want to add pepperon, Y or N? ")
addExtraCheese = input("Do you want to add extra cheese, Y or N? ")

totalBill = ""

if (size == "S"):
    totalBill = 15
    if (addPepperoni == "Y"):
        totalBill += 2
    else:
        totalBill = totalBill
    if (addExtraCheese == "Y" ):
        totalBill += 1
        print(f"Your total bill is ${totalBill}")
    else:
        totalBill = totalBill
        print(f"Your total bill is ${totalBill}")
elif (size == "M"):
    totalBill = 20
    if (addPepperoni == "Y"):
        totalBill += 3
    else:
        totalBill = totalBill
    if (addExtraCheese == "Y"):
        totalBill += 1
        print(f"Your total bill is ${totalBill}")
    else:
        totalBill = totalBill
        print(f"Your total bill is ${totalBill}")
        
elif (size == "L"):
    totalBill = 25
    if (addPepperoni == "Y"):
        totalBill += 3
    else:
        totalBill = totalBill
    if (addExtraCheese == "Y" ):
        totalBill += 1
        print(f"Your total bill is ${totalBill}")
    else:
        totalBill = totalBill
        print(f"Your total bill is ${totalBill}")
