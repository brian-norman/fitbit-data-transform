# Fitbit Data Transform
This is a utility I used to take the Fitbit JSONs when exporting weight logs from Fitbit.com and turning them into my own JSON for personal use. This utility currently just combines all their JSONs into one, and strips away all the fields except for weight and date. 

## Usage
Export data from fitbit.com and place all their generated weight JSONs into the /weight-jsons folder. These files will look like `weight-year-month-day.json`. 
Then run `python merge_jsons.py` which will generate a `merged.json` file which you can use!
