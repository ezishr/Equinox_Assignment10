from dataloadingPackage.data_loading import *
import pandas as pd
import csv

data = data_loading_function()

headers = data[0].keys()

csv_file = 'data.csv'

with open(csv_file, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    for row in data:
        writer.writerow(row)