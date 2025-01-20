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
        a,b=self.a,self.b
#start a while loop when b doesn’t equals to 0        
        while b!=0:
#replace a by the remainder of a%b
            a=a%b
#exchange the values               
            a,b=b,a
#return gcd            
        return a
    
num1=int(input("please enter the first number"))
num2=int(input("please enter the second number"))
get_gcd=EuclideanAlgorithm(num1,num2)
#calling the calculate_gcd method
result=get_gcd.calculate_gcd()
print(result)
