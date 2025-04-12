#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 16:10:26 2025

@author: shaique
"""

def even_odd_checker(x):
    
    if (x <= 0):
        
        return "invalid"
    
    if(x%2==0):
        
        return "even"
    
    else:
        
        return "odd"
        
    return type

x = int(input("Enter a positive integer != 1: "))

seq = []

while x!=1:
    
    seq.append(x)
    
    type = even_odd_checker(x)
    
    if type == "even":
        
        x = x/2
        
    elif type == "odd": 
        
        x = (3*x) + 1
        
    else:
        
        print("You either entered 0 or a negative number, please enter a natural number")
        
        break
        
    if x==1:
        
        seq.insert(len(seq), 1)
        
        break
    
print("The sequence for the inputted number is: " , seq)

print("THe problem is the famous Collatx conjecture also know as 3x+1 conjecture or the Syracuse Problem, Which states that ecvery natural number will have a sequence terminating at 1, which will then cuycle through values 1 , 4 ,2 indefinitely")

print("Souces:")

print("https://terrytao.wordpress.com/wp-content/uploads/2020/02/collatz.pdf")

print("https://arxiv.org/pdf/math/0608208")

print("Veritasim Video link : https://www.youtube.com/watch?v=094y1Z2wpJg")

print("Therefore the answer is that no such natural number exists for which this will never happen.")    