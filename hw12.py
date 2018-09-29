#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 23:42:29 2018

@author: santhoshreddyventeru
"""
import requests
import re
from bs4 import BeautifulSoup
url = "http://cs.siu.edu/faculty-staff/continuing_faculty.php"  # connects to th university site using this url
r = requests.get(url)
x = r.text
def homework12():
        parse_r = BeautifulSoup(x, 'html.parser')
        facult_y = parse_r.find_all('div', class_='people-wrapper')
        #print(facult_y)
        for facult_y in facult_y:
            faculty_soup = BeautifulSoup(str(facult_y), 'html.parser')
            faculty_list = faculty_soup.get_text().split('\n') 
            #print(faculty_list)
            #print(len(faculty_list))
            faculty_list  = [i for i in faculty_list if i != '']
            #print(faculty_list[1])
            """
            qw = len(faculty_list)
            for i in range(qw):
                print(faculty_list[i])
                print("\n")
                print("----------")
            """
            
            print('Name: ', faculty_list[0])
            print('Position: ', faculty_list[1])
            #print('office', faculty_list[2])
            
            if faculty_list[2].find('Email') != -1:
                #print("name")
                print(re.search(r'Phone:.*[0-9]', faculty_list[2]).group(0))
                print(re.search(r'Email:.*edu', faculty_list[2]).group(0))
                print(re.search(r'Office:.*P', faculty_list[2]).group(0))
                
            
            else:
                print(faculty_list[3], faculty_list[2], sep='\n')
                if(len(faculty_list) > 4):
                    #print("y")
                    print(faculty_list[4])
        
            
            if faculty_list[-1].find('homepage:') != -1:
                print("x")
                #print(re.search(r'homepage:.*', faculty_list[-1]).group(0))
            else:
                print('homepage: NA')
            print('==========================================')

if __name__ == "__main__":
    homework12()