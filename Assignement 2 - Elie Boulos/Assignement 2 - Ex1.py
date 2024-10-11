# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 18:50:01 2024

@author: User
"""
list1 = [54,76,2,4,98,100]
first_number= int(input('enter the first number'))
second_number= int(input('enter the second number'))
for i in list1:
    if (i>=first_number and i<=second_number) or (i<=first_number and i>=second_number) :
     print(i)
    