import json

with open('sample2.json', 'r', encoding='utf8') as json_file:
    data = json.load(json_file)

for person in data['people']:
    if person['has_licence'] == False:
        del person['has_licence']

with open('sample2_copy.json', 'w', encoding='utf8') as json_file_2:
    json.dump(data, json_file_2, indent=2)