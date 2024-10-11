# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 20:03:36 2024

@author: User
"""

numbers = [-12, 4, 12, 25, 67]
repeat = True

while repeat==True:
    enter_number = int(input('Enter a number '))
    numbers.append(enter_number)
    numbers.sort()
    print(numbers)
    
    if enter_number==-99:
        repeat=False