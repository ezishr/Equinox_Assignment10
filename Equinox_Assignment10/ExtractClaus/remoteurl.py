# File Name: remoteurl.py
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


def get_url_organization(index, data):
    """
    Print the URL and organization of a data repository from the JSON data with selected index.
    @param index int: The index of the data repository in the JSON data.
    @param data list: The list of dictionaries containing the JSON data.
    """

    # Check if the index is valid
    if index < 0 or index >= len(data):
        print(f'There is no data at row {index}')
    else:
        print("URL: "+data[index]["remote_url"]) # Print the URL of the data repository
        print("Organization: "+data[index]["organization"]) # Print the organization of the data repository



