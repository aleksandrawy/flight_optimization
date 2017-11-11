import json

with open("airports.geojson", encoding='utf-8') as input_file:
    old_data = json.load(input_file)

output_dict = old_data["features"]
output = []
for i in output_dict:
    output.append(i["properties"])

out = []

for i in output:
    if i["country"] == "Switzerland" or i["country"] == "Italy" or i["country"] == "United Kingdom" or i["country"] \
            == "Austria" or i["country"] == "Spain" or i["country"] == "Germany" or i["country"] == "Belgium" or i["country"] \
            == "France" or i["country"] == "Netherlands" or i["country"] == "Slovenia" or i["country"] == "Sweden" \
            or i["country"] == "Denmark" or i["country"] == "Moldova" or i["country"] == "Finland" or i["country"] == "Slovakia"\
            or i["country"] == "Macedonia" or i["country"] == "Albania" or i["country"] == "Norway" or i["country"] \
            == "Croatia" or i["country"] == "Lithuania" or i["country"] == "Bosnia and Herzegovina" or i["country"] \
            == "Poland" or i["country"] == "Czech Republic" or i["country"] == "Portugal" or i["country"] == "Armenia" \
            or i["country"] == "Hungary" or i["country"] == "Cyprus" or i["country"] == "Serbia" or i["country"] == "Montenegro" \
            or i["country"] == "Romania" or i["country"] == "Greece" or i["country"] == "Ireland" or i["country"] == "Estonia" \
            or i["country"] == "Turkey" or i["country"] == "Latvia" or i["country"] == "Bulagria" or i["country"] \
            == "Georgia" or i["country"] == "Malta":
        out.append(i)

with open("eurocontrol.json", "w") as output_file:
    json.dump(out, output_file, indent=4)