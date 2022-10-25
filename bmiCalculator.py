# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 07:32:56 2022

@author: Theophilus
"""

weight = int(input("Enter your weight in kg: "))
height = int(input("Enter your height in metres: "))

bmi = int(weight/(height**2))


print(f"Your bmi is {bmi}")

