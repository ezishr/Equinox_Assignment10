# File Name: extract.py
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


def getbasicinformation(index, data):
    """
    This function prints basic information including category, file name, and visibility about a data repository from the JSON data.
    @param index int: The index of the data repository in the JSON data.
    @param data list: The list of dictionaries containing the JSON data.
    """
    
    # Check if the index is valid
    if index < 0 or index >= len(data):
        print("Index out of range.")
        return None
    else:
        print('Category: ' + data[index]['category']) # Print the category of the data repository
        print('File Name: ' + data[index]['file_name']) # Print the file name of the data repository
        print('Is it visible?: ' + str(data[index]['visible'])) # Print whether the data repository is visible or not
