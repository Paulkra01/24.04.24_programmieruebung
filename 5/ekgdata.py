import json
import pandas as pd
import numpy as np
import plotly as pl

# %% Objekt-Welt

# Klasse EKG-Data für Peakfinder, die uns ermöglicht peaks zu finden

class EKGdata:

    @staticmethod
    def load_by_id(search_id):
        file = open("data/person_db.json")
        person_data = json.load(file)
        if search_id == "None":
            return {}

        for person in person_data:
            for ekg_test in person["ekg_tests"]:
                if ekg_test["id"] == search_id:
                    return ekg_test
            
        return {}


    @staticmethod
    def find_peaks(person_data, threshold, respacing_factor=5):
        """
        A function to find the peaks in a series
        Args:
            - series (pd.Series): The series to find the peaks in
            - threshold (float): The threshold for the peaks
            - respacing_factor (int): The factor to respace the series
        Returns:
            - peaks (list): A list of the indices of the peaks
        """
        file = open("data/person_db.json")
        person_data = json.load(file)

       
        # Respace the series
        person_data = person_data.iloc[::respacing_factor]
        
        # Filter the series
        person_data = person_data[person_data>threshold]


        peaks = []
        last = 0
        current = 0
        next = 0

        for index, row in person_data.items():
            last = current
            current = next
            next = row

            if last < current and current > next and current > threshold:
                peaks.append(index-respacing_factor)

        return peaks
    @staticmethod
    def estimate_hr():
        pass

    @staticmethod
    def plot_time_series():
        pass

## Konstruktor der Klasse soll die Daten einlesen

    def __init__(self, ekg_dict):
        #pass
        self.id = ekg_dict["id"]
        self.date = ekg_dict["date"]
        self.data = ekg_dict["result_link"]
        self.df = pd.read_csv(self.data, sep='\t', header=None, names=['Messwerte in mV','Zeit in ms',])


    def make_plot(self):

        # Erstellte einen Line Plot, der ersten 2000 Werte mit der Zeit aus der x-Achse
        self.fig = px.line(self.df.head(2000), x="Zeit in ms", y="Messwerte in mV")
        # return self.fig


if __name__ == "__main__":
    # print("This is a module with some functions to read the EKG data")
    file = open("data/person_db.json")
    person_data = json.load(file)
    ekg_dict = person_data[0]["ekg_tests"][0]
    # print(ekg_dict)
    ekg = EKGdata(ekg_dict)
    # print(ekg.df.head())
    print(EKGdata.load_by_id(1))




# %% Funktionen

        
@staticmethod
def find_peaks():
    file = open("data/person_db.json")
    person_data = json.load(file)
    for person in person_data:
            for ekg_test in person["ekg_tests"]:
                    if ekg_test["id"] == id:
                        ekg = EKGdata(ekg_test)
                        peaks = find_peaks(ekg.df['Messwerte in mV'], distance=100)
                        ekg.df['Peaks'] = np.nan
                        ekg.df.loc[peaks, 'Peaks'] = ekg.df.loc[peaks, 'Messwerte in mV']
                        peaks_list = ekg.df['Peaks'].tolist()

                    return " das sind die peaks" + peaks_list

