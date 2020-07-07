import json
import glob
from datetime import date


def compare_date(weight_json):
    """Extracts date of weight JSON object for sorting purposes"""
    # What I'm working with: "04/22/14"
    month = weight_json['date'][:2]
    day = weight_json['date'][3:5]
    year = "20" + weight_json['date'][6:]
    return date.fromisoformat(f"{year}-{month}-{day}")

def strip(weight_json):
    """Keeps only date and weight in JSON"""
    new = {wanted_key: weight_json[wanted_key] for wanted_key in ['weight', 'date']}
    return new
    
def get_weights():
    """Get every JSON object of weight from every JSON file in /weight-jsons"""
    paths = glob.glob('./weight-jsons/*.json')
    weight_jsons = []
    for path in paths:
        with open(path, 'r') as json_file:
            json_data = json_file.read()
            arr = json.loads(json_data)
            weight_jsons += arr
    return weight_jsons

def write_merged(weight_jsons):
    """Write to merged.json all these sorted weights"""
    first_item = True
    with open('merged.json', 'w') as output_file:
        output_file.write('[\n')
        for weight_json in weight_jsons:
            if first_item:
                output_file.write(json.dumps(weight_json))
                first_item = False
            else:
                output_file.write(",\n" + json.dumps(weight_json))
        output_file.write("\n]")

def merge_jsons():
    """Merges every JSON in /weight-jsons into merged.json, stripping unncessary fields"""
    weight_jsons = get_weights()
    weight_jsons = list(map(strip, weight_jsons))
    weight_jsons.sort(key=compare_date, reverse=True)
    write_merged(weight_jsons)


if __name__ == "__main__":
    """
    The Fitbit website's export returns a different csv for every month of data
    so in order to use it as one JSON, they need to all be merged. The data also
    comes with a bunch of extra uninteresting fields, so I also strip the JSON
    objects down to just weight and date.

    Usage: Place all the JSONs in a single directory called /weight-jsons
    Returns: Nothing, but does create/update merged.json with the weights sorted

    TODO: let user pass in directory that has all the weight jsons
    TODO: let the user specify which fields to keep in the merged output
    """
    merge_jsons()
