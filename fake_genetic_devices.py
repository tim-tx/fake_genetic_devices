import csv
import json
from random import choice


names = set()
output = []

with open('FPvisualization/FPs_processed.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        names.add(row[0])

it = iter(names)
for i in range(64):
    output.append({
        "collection": "output_reporters",
        "name": next(it) + "_reporter",
        
    })

for i in range(64):
    output.append({
        "collection": "output_structure",
        "gate_name": output[i]['name'],
        "devices": [
            { "name": output[i]['name'],
              "components": [
                  "#promoter?",
                  "#promoter?",
                  output[i]['name'].rstrip("reporter") + "cassette"
              ]
            }
        ] 
    })
    
for i in range(64):
    output.append({
        "collection": "parts",
        "type": "cassette",
        "name": output[i]['name'].rstrip("reporter") + "cassette",
        "dnasequence": ''.join(choice('ATGC') for i in range(64))
    })

with open("Eco.64dummy.output.json", "w") as output_file:
    output_file.write(json.dumps(output, indent=4))
