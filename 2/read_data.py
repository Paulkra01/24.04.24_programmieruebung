import json


def get_person_list():
    # Opening JSON file
    file = open("../data/person_db.json")
    # Loading the JSON File in a dictionary
    person_data = json.load(file)
    Names = []

    for i in person_data:
        name = [i["lastname"] + ", " +  i["firstname"]]
        Names.append(name)
    return Names

