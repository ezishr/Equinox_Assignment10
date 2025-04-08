# File Name: main.py
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

from ExtractClaus.remoteurl import *
from extractPackage.extract import *
from convertJSONtoCSV.JSON_to_CSV import *
from dataloadingPackage.data_loading import *
import random

if __name__ == '__main__': # Entry point
    # Load the data from the JSON file
    data = data_loading_function()

    # Get random index
    index = random.randint(0, len(data) - 1)

    # Test the getbasicinformation function. Expected output is the category, file name, and visibility of the data repository at the given index.
    getbasicinformation(index, data)
    
    # Test the get_url_organization function. Expected output is the URL and organization of the data repository at the given index.
    get_url_organization(index, data)

    # Test the convert_json_to_csv function. Expected output is a CSV file with the data from the JSON file, staying in CSV data folder.
    convert_json_to_csv(data)