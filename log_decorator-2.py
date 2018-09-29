#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on fri Apr  8 23:39:15 2018

@author: santhoshreddyventeru
"""

import time
import sys


def log(file_Path = None):
    def log_decorator(func):
        def wrapper(*args, **kwargs):
           
            if file_Path:
                if isinstance(file_Path,str):
                #if path(file_path,str)
                    try:
                        
                        fp = open(file_Path,"a+")
                        #fp = open(file_Path,"w+")
                    except:
                        fp = sys.stdout
                else:
                    fp = sys.stdout
            else:
                fp = sys.stdout
           
            fp.write("************************************************"+"\n")
           
            fp.write("calling function {}.".format(func.__name__)+"\n")
            if args:
                fp.write("Arguments:" + "\n")
                typ_e = ""
                for each in args:
                    typ_e = type_of_arg(each)
                    fp.write(" - {} of type {}".format(each,typ_e) + "\n")
            else:
                fp.write("No arguments" + "\n")
            fp.write("Output:" + "\n")
            start = time.time()
            
            result = func(*args, **kwargs)
            endtime_ = time.time()
            
            
            
            el_time = endtime_ - start
            fp.write("Execution Time: {0:.5f} s".format(round(el_time,5)) + "\n")
            if result:
                type_ = ""
                type_ = type_of_arg(result)
                fp.write("Return value: {} of type {}.".format(result,type_) + "\n")
                #fp.write("************************************************" + "\n")

            else:
                fp.write("No return value." + "\n")
                
            fp.write("************************************************" + "\n")
        return wrapper 
    return log_decorator


def type_of_arg(arguments):
    x = ""
    
    if isinstance(arguments,int):       #checks for int 
        x = "int"
        
    if isinstance(arguments,list):      #checks for list  
        x = "list"
        
    if isinstance(arguments,dict):      #checks for dict
        x = "dict"
        
    if isinstance(arguments,tuple):     #checks for tuple
        x = "tuple"
           
    if isinstance(arguments,str):       #checks for str
        x = "str"
    
    if isinstance(arguments,float):     #checks for float
        x = "float"
        
    if isinstance(arguments,bool):      #checks for bool
        x = "bool"
        
    if isinstance(arguments,set):       #checks for set
        x = "set"
    
    if isinstance(arguments,complex):   #checks for complex
        x = "complex"
        
    
    return x




@log()
def factorial(*num_list):
    results = []
    for number in num_list:
        res = number
        for i in range(number-1,0,-1):
            res = i*res
        results.append(res)
    return results



"""
This function logs is written into log.txt file
"""
@log("/users/santhoshreddyventeru/Documents/python/log.txt")
def waste_time(a, b, c):
    print("Wasting time.")
    time.sleep(5)
    return a, b, c


"""
This function logs is written into log.txt file
"""
@log("/users/santhoshreddyventeru/Documents/python/log.txt") 
def gcd(a, b):
    print("The GCD of", a, "and", b, "is ", end="")
    while a!=b:
        if a > b:
            a -= b 
        else:
            b -= a
    print(abs(a))
    return abs(a)      


@log()
def print_hello():
    print("hello!!!")
   
      
@log(10)
def print_goodbye():
    print("goodbye.")
    
      
    
if __name__ == "__main__":
    factorial(4,5)
    waste_time("one", 2, "3")
    gcd(15,9)
    print_hello()
    print_goodbye()