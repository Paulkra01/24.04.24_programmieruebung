import json
import datetime as dt

class Person:
    
    @staticmethod
    def load_person_data():
        """A Function that knows where te person Database is and returns a Dictionary with the Persons"""
        file = open("../data/person_db.json")
        person_data = json.load(file)
        return person_data

    @staticmethod
    def get_person_list(person_data):
        """A Function that takes the persons-dictionary and returns a list auf all person names"""
        list_of_names = []

        for eintrag in person_data:
            list_of_names.append(eintrag["lastname"] + ", " +  eintrag["firstname"])
        return list_of_names
    
    @staticmethod
    def find_person_data_by_name(suchstring):
        """ Eine Funktion der Nachname, Vorname als ein String übergeben wird
        und die die Person als Dictionary zurück gibt"""

        person_data = Person.load_person_data()
        #print(suchstring)
        if suchstring == "None":
            return {}

        two_names = suchstring.split(", ")
        vorname = two_names[1]
        nachname = two_names[0]

        for eintrag in person_data:
            print(eintrag)
            if (eintrag["lastname"] == nachname and eintrag["firstname"] == vorname):
                print()

                return eintrag
        else:
            return {}
        
    
    
        
    def __init__(self, person_dict) -> None:
        self.date_of_birth = person_dict["date_of_birth"]
        self.firstname = person_dict["firstname"]
        self.lastname = person_dict["lastname"]
        self.picture_path = person_dict["picture_path"]
        self.id = person_dict["id"]
        self.age_years = self.calc_age()
        # self.sex = sex
        
    @staticmethod
    def calc_age(self):
        today = dt.today()
        birth_date = dt.strptime(self.date_of_birth, "%Y-%m-%d")
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age
    
    @staticmethod
    def calc_max_heart_rate(self):
        if self.sex == "male":
            max_hr_bpm =  223 - 0.9 * self.age_years
        elif self.sex == "female":
            max_hr_bpm = 226 - 1.0 *  self.age_years
        else:
            # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
            max_hr_bpm  = input("Enter maximum heart rate:")
        return int(max_hr_bpm)

    @staticmethod
    def load_by_id(search_id):
        file = open("../data/person_db.json")
        person_data = json.load(file)
        if search_id == "None":
            return {}

        for person in person_data:
            if person["id"] == search_id:
                return person
            
        return {}


if __name__ == "__main__":
    # print("This is a module with some functions to read the person data")
    persons = Person.load_person_data()
    person_names = Person.get_person_list(persons)
    # print(person_names)
    # print(Person.find_person_data_by_name("Huber, Julian"))
    # print(Person.load_by_id(1)["lastname"])