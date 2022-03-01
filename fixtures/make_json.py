import csv
import json


def new_json_file(json_, csv_, field_names):
    csv_file = open(csv_, 'r')
    json_file = open(json_, 'w', encoding='utf-8')
    reader = csv.DictReader(csv_file, field_names)
    result = json.dumps([row for row in reader])
    return json_file.write(result)


field_names_1 = ("id", "name", "author", "price", "description", "address", "is_published")
field_names_2 = ("id", "name")

new_json_file("ads.json", "ads.csv", field_names_1)
new_json_file("categories.json", "categories.csv", field_names_2)