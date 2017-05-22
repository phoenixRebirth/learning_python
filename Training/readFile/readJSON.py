
import json
import sys
import os

def open_json(filename):
    try:
        f = open(filename, 'r')
    except FileNotFoundError:
        print('File ' + filename + ' not found')
        exit()

    data = f.read()

    try:
        parsed_data = json.loads(data)
    except json.decoder.JSONDecodeError as e:
        print('Could not read file:\n' + str(e))
        exit()

    return parsed_data


os.system('pwd')
parsed_data = open_json(sys.argv[1])
print(parsed_data)


# python readJSON.py /Users/christophesilhouette/Documents/projects/pierreIrisDetection/IrisDetection/data/confs/SVMcomparisonInputParameters.json
# python readJSON.py /Users/christophesilhouette/Documents/projects/pierreIrisDetection/IrisDetection/data/confs/SVMcomparisonInputParameters.json
