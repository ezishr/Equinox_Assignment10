# File Name: JSON_to_CSV.py
# Student Name: Annapoorna Nair, Will Claus, Chrystie Cadet, Eirlys Vo
# Email: nairap@mail.uc.edu, clausws@mail.uc.edu, cadetce@mail.uc.edu, vopq@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: April 10, 2025
# Course #/Section: IS 4010 - 001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Choose an API to read and extract data. Convert it to CSV format.
# Brief Description of what this module does: Work with API and load JSON data.
# Citations: https://docs.python.org/3/library/csv.html
# Anything else that's relevant: N/A

import csv

def convert_json_to_csv(data, file_name):
    """
    Convert the JSON data to CSV format.
    @param data list: The list of dictionaries containing the JSON data.
    @param file_name string: Name of the dataset in CSV.
    """

    # Get the headers from the first dictionary in the list
    headers = data[0].keys()

    # Create a CSV file and write the data to it
    csv_file = f'dataPackage/{file_name}.csv'

    with open(csv_file, 'w', newline='') as f:
        # Create a CSV writer object
        csv_writer = csv.DictWriter(f, fieldnames=headers)
        csv_writer.writeheader()
        # Add each data row to the CSV file
        for row in data:
            csv_writer.writerow(row)