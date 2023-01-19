import json
import sys


# Bypass dictionary
def bypass(d):
    if isinstance(d, list):
        for elm in d:
            bypass(elm)
    if isinstance(d, dict):
        if 'id' in d:
            for elm in json_change['values']:
                if d['id'] == elm['id']:
                    d.update(elm)
                    break
        if 'values' in d:
            for sub_d in d['values']:
                bypass(sub_d)


with open(sys.argv[1], 'r') as f:
    json_input = json.load(f)

with open(sys.argv[2], 'r') as f:
    json_change = json.load(f)

bypass(json_input['tests'])

with open('report.json', 'w') as f:
    json.dump(json_input, f)


