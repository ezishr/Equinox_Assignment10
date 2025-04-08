# File Name: data_loading.py
# Student Name: Annapoorna Nair, Will Claus, Chrystie Cadet, Eirlys Vo
# Email: nairap@mail.uc.edu, clausws@mail.uc.edu, cadetce@mail.uc.edu, vopq@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: April 10, 2025
# Course #/Section: IS 4010 - 001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Choose an API to read and extract data. Convert it to CSV format.
# Brief Description of what this module does: Work with API and load JSON data.
# Citations: N/A
# Anything else that's relevant: N/A


import json
import requests

def data_loading_function():
    """
    This function loads data from a remote URL and parses the JSON response.
    @return dict: A dictionary containing the parsed JSON data.
    """

    # URL to fetch data and get content from NASA - Open Science Data Repository
    response = requests.get('https://osdr.nasa.gov/osdr/data/osd/files/87')
    json_string = response.content

    # Parse the JSON string into a Python dictionary
    parsed_json = json.loads(json_string) 

    # Extract the relevant data from the parsed JSON
    data = parsed_json['studies']['OSD-87']['study_files']

    return data

    

   

