#!/usr/bin/env python

import json
import csv

# Define a function
def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []

    # Read csv file
    with open(csvFilePath, encoding='utf-8') as csvf:
        # load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)

        # convert each csv row into python dict
        for row in csvReader:
            # add this python dict to json array
            jsonArray.append(row)

    # convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=2)
        jsonf.write(jsonString)

# Define the files
csvFilePath = r'csv_data.csv'
jsonFilePath = r'data.json'

# Call the function
csv_to_json(csvFilePath, jsonFilePath)