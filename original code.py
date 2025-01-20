#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 22:09:43 2025

@author: caoxufei
"""
#define the class
class EuclideanAlgorithm:
#initialize a and b
    def __init__(self,a,b): 
        self.a=a
        self.b=b
#calculate gcd   
    def calculate_gcd(self):
#start a while loop when b doesn’t equals to 0        
        while self.b!=0:
#replace a by the remainder of a%b
           self.a,self.b=self.b,self.a%self.b
#return gcd            
        return self.a
#check if the input a positive integer    
    def get_number(self):
#if inputs are not integers,return False
       if not isinstance(self.a,int):
           return False
       if not isinstance(self.b,int):
           return False 
#if inputs are negative or equals to 0, return False
       if self.a<=0 or self.b<=0:
           return False
#if inputs are positive integers, return True
       else:
           return True
#ask for inputs       
try:
    num1=int(input("please enter the first number"))
    num2=int(input("please enter the second number"))
    get_gcd=EuclideanAlgorithm(num1,num2)
#check if the inputs valid
    if get_gcd.get_number() == False:
       print("please enter a positive integer")
    else:
       print(f"gcd is {get_gcd.calculate_gcd()}")
except ValueError:
    print("invalid input,please enter a pisitive integer")
