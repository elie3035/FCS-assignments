# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 20:32:42 2024

@author: User
"""

names = ['Maria', 'Hala', 'Ghady', 'Ehsan', 'Joe', 'Zoe']
repeat = True

while repeat:
    enter_letter = input('Enter a letter: ')
    
    for name in names:
        if enter_letter in name:  
            print(name)
    
    add_letter = input('Do you want to add another letter? (y/n): ')
    
    if add_letter== 'n':  
        repeat = False