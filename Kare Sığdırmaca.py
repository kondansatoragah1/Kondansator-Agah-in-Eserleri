# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 08:45:37 2022

@author: Acer
"""


while True:
    a=int(input("Enter first value for suitcase:..."))
    b=int(input("Enter second value for suitcase:..."))
    c=int(input("Enter  value for square 1:..."))
    d=int(input("Enter  value for square 2:..."))
    iht=c+d
    if iht<=a:
        print("You can travel")
        continue
    
    elif iht<=b:
        print("You can travel")
        continue
    else:
        print("You can not travel")
        continue