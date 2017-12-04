import json
from collections import OrderedDict

with open("waypoints.geojson", encoding='utf-8') as input_file:
    old_data = json.load(input_file)

output_dict = old_data["features"]
output = []
for i in output_dict:
    output.append(i['properties']['Name'])
    output.append(i['geometry'])

print(output)
out = []

up = 71.671710
down = 35.281454
left = -12.299279
right = 36.949231

s = []
for i in output_dict:
    if down < i['geometry']['coordinates'][1] < up and left < i['geometry']['coordinates'][0] < right:
        if (i['geometry']['coordinates'] not in s):
            s.append(i['geometry']['coordinates'])
            out.append(i)




with open("waypoints_filtered.json", "w") as output_file:
    json.dump(out, output_file, indent=4)