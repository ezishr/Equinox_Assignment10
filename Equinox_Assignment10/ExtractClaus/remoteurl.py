# File Name : remoteurl.py
# Student Name: Will Claus
# email:  clausws@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:   April 10, 2025
# Course #/Section:   IS 4010 Section 1
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  We are to work with APIs and Json

# Brief Description of what this module does: This module should build a url with a data request and submit it to the API server.
# Citations: I mainly just used the work we did in class to make this and my group mate's suggestion

# Anything else that's relevant:



# Import dataloadingPackage to get the data
from dataloadingPackage.data_loading import *
data = data_loading_function()

def get_url_organization(index):
    print("URL: "+data[index]["remote_url"])
    print("Organization: "+data[index]["organization"])



