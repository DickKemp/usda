# USDA food data 
exploring the USDA food data with python

## Data sources
USDA data downloads:  https://fdc.nal.usda.gov/download-datasets.html

Downloaded and unzipped the foundational foods JSON data from here:

https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_foundation_food_json_2021-10-28.zip

This provided some information about the data format and contents:
https://fdc.nal.usda.gov/docs/Foundation_Foods_Documentation_Oct2021.pdf

This was most useful, the data dictionary for the various fields:  https://fdc.nal.usda.gov/portal-data/external/dataDictionary

the foundational food download did not appear to be useful, so I downloaded the branded data from:  https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_branded_food_json_2021-10-28.zip

this was a 2.6Gb json file after unzipping

## processing to extract relevant fields from the branded foods json file
* the branded food json file was used
* we want to pick out relevant fields for each food item and write them into a separate file, which can then be used by an application
* given that branded foods is several GBs, we do not want to load the entire json into memory using json.load().  We use a utility that I wrote to read the json list one by one, only keeping a single object in memory as it reads through the data
* the ipynb demostrates use of a utility jsonstream to read the json list contained within the branded foods json file
* for each food item in the list, call a method to pick the fields of interest and write those out to an output CSV file


