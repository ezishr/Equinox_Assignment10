# File Name : Extract.py
# Student Name: Chrystie Cadet
# email: cadetce@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:  4/10/25
# Course #/Section: IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment:
# Brief Description of what this module does: 
# Citations: 

from dataloadingPackage.data_loading import *

data = data_loading_function()

def getbasicinformation(index):
    print('Category: '+data[index]['category'])
    print('File Name: '+data[index]['file_name'])
    print('Is it visible?: '+str(data[index]['visible']))
