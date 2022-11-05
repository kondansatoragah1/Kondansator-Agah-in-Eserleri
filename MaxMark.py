# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 08:39:13 2022

@author: OMER
"""

maximummark=0
currentmark=0
stdnamemax=""
currentstdname=""

numberofstds=0

numberofstds=int(input("Please enter the student number "))

for x in range(0,numberofstds,1):
      currentstdname = input("Please enter the student name ")
      currentmark = int(input("Please enter the student's mark "))
      if currentmark > maximummark:
            maximummark = currentmark
            stdnamemax = currentstdname
      
print("Maximum mark is " + str(maximummark))
print("Student's name who has the maximum mark is " + stdnamemax)
      
