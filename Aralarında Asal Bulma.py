# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 08:42:32 2022

@author: Acer
"""

ca=0
cb=0
while True:
    a=int(input("Enter first value"))
    b=int(input("Enter second value"))
    for i in range(1,a):
        if a%i==0:
            ca+=1
    for i in range(1,b):
        if b%i==0:
            cb+=1
    if ca==cb:
        print("They are coprime")
        continue
    else:
        print("They are not coprime")
        continue
    