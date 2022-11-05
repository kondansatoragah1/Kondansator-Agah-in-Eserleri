# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 09:10:54 2022

@author: OMER
"""
smallernumber=input("Please enter number of stds: ")
biggernumber=input("Please enter number of stds: ")


smallernumber = int(smallernumber)
biggernumber=int(biggernumber)
counter=0

while smallernumber<=biggernumber:
      
      for x in range(2,smallernumber+1,1):
            
            if smallernumber % x == 0:
                  counter = counter +1
      if counter==1:
            print("My number is prime number "+ str(smallernumber))
      
      counter = 0
      
      smallernumber = smallernumber + 1













