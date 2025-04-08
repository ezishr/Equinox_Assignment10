# File Name : data_loading.py
# Student Name: Annapoorna Nair
# email:  nairap@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:   April 10, 2025
# Course #/Section:   IS 4010 Section 1
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  We are to work with APIs and Json

# Brief Description of what this module does: This module should build a url with a data request and submit it to the API server.
# Citations: I mainly just used the work we did in class to make this and my group mate's suggestion

# Anything else that's relevant:


import json
import requests

def data_loading_function():
    response = requests.get('https://osdr.nasa.gov/osdr/data/osd/files/87')
    json_string = response.content

    parsed_json = json.loads(json_string) 

    data = parsed_json['studies']['OSD-87']['study_files']

    return data

    

   

