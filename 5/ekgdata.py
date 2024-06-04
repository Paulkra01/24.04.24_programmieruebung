import json
import pandas as pd
import numpy as np
import plotly as pl
import plotly.express as px

# %% Objekt-Welt

# Klasse EKG-Data für Peakfinder, die uns ermöglicht peaks zu finden

class EKGdata:

    @staticmethod
    def load_by_id(search_id, ekg_test=1):
        file = open("data/person_db.json")
        person_data = json.load(file)
        if search_id == "None":
            return {}

        for person in person_data:
            for ekg_test in person["ekg_tests"]:
                if ekg_test["id"] == search_id:
                    return ekg_test


    @staticmethod
    def find_peaks(search_id, ekg_test=1,respacing_factor= 5, threshold= 0.5):
    
        file = open("data/person_db.json")
        person_data = json.load(file)
        if search_id == "None":
            return {}

        for person in person_data:
            for ekg_test in person["ekg_tests"]:
                if ekg_test["id"] == search_id:
                    result_link = pd.read_csv(ekg_test["result_link"], sep='\t', header=None, names=['Messwerte in mV','Zeit in ms'])
                    
        result_link = result_link.iloc[::respacing_factor]
        
        # # # Filter the series
        result_link = result_link[result_link>threshold]
        peaks = []
        last = 0
        current = 0
        next = 0

        for index, row in result_link.iterrows():
            last = current
            current = next
            next = row['Messwerte in mV']

            if last < current and current > next and current > threshold:
             peaks.append(index-respacing_factor)
        return peaks            
        #data = EKGdata.load_by_id(search_id=1,ekg_test=1)
        # Respace the series
        # result_link = result_link.iloc[::respacing_factor]
        
        # # # Filter the series
        # result_link = result_link[result_link>threshold]
        # respacing_factor = 5
        # threshold = 0.5
        # peaks = []
        # last = 0
        # current = 0
        # next = 0

        # for index, row in result_link():
        #     last = current
        #     current = next
        #     next = row

        #     if last < current and current > next and current > threshold:
        #          peaks.append(index-respacing_factor)

        # return peaks 
        
    @staticmethod
    def estimate_hr(peaks, result_link):


        peaks = EKGdata.find_peaks(peaks)
        result_link = EKGdata.find_peaks(result_link)
        time = int(len(result_link) / 1000 / 60)
        heart_rate = len(peaks) / time
    
        print(heart_rate)

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
        self.peaks = []

    def make_plot(self):

        # Erstellt einen Line Plot, der ersten 2000 Werte mit der Zeit aus der x-Achse
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
    # print(EKGdata.load_by_id(1))
    # print(EKGdata.find_peaks(1))

# %% Funktionen

        

