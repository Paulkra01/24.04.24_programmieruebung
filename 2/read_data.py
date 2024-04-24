import json


def get_person_list():
    # Opening JSON file
    file = open("../data/person_db.json")
    # Loading the JSON File in a dictionary
    person_data = json.load(file)
    Names = []

    for i in person_data:
        name = i['lastname'] + ", " +  i['firstname']
        Names.append(name)
    return Names


def find_person_data_by_name(suchstring):

    file = open("../data/person_db.json")
    person_data = json.load(file)
    if suchstring == "None":
        return {}

    two_names = suchstring.split(", ")
    vorname = two_names[1]
    nachname = two_names[0]

    for i in person_data:
        print(i)
        if (i["lastname"] == nachname and i["firstname"] == vorname):
            print()

            return i
    else:
        return {}