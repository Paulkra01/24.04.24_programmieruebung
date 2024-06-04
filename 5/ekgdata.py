import json
import pandas as pd
import numpy as np
import plotly as pl
import plotly.express as px
import plotly.graph_objects as go

# %% Objekt-Welt

# Klasse EKG-Data für Peakfinder, die uns ermöglicht peaks zu finden

class EKGdata:

## Konstruktor der Klasse soll die Daten einlesen

    def __init__(self, ekg_dict):
        self.id = ekg_dict["id"]
        self.date = ekg_dict["date"]
        self.result_link = ekg_dict["result_link"]
        self.df = pd.read_csv(self.result_link, sep='\t', header=None, names=['Messwerte in mV','Zeit in ms',])
        self.peaks = []

    def make_plot(self):

        # Erstellt einen Line Plot, der ersten 2000 Werte mit der Zeit aus der x-Achse
        self.fig = px.line(self.df.head(2000), x="Zeit in ms", y="Messwerte in mV")
        # return self.fig

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


    # @staticmethod
    # def find_peaks(search_id, ekg_test=1,respacing_factor= 5, threshold= 0.5):
    
    #     file = open("data/person_db.json")
    #     person_data = json.load(file)
    #     if search_id == "None":
    #         return {}

    #     for person in person_data:
    #         for ekg_test in person["ekg_tests"]:
    #             if ekg_test["id"] == search_id:
    #                 result_link = pd.read_csv(ekg_test["result_link"], sep='\t', header=None, names=['Messwerte in mV','Zeit in ms'])
                    
    #     result_link = result_link.iloc[::respacing_factor]
        
    #     # # # Filter the series
    #     result_link = result_link[result_link>threshold]
    #     peaks = []
    #     last = 0
    #     current = 0
    #     next = 0

    #     for index, row in result_link.iterrows():
    #         last = current
    #         current = next
    #         next = row['Messwerte in mV']

    #         if last < current and current > next and current > threshold:
    #          peaks.append(index-respacing_factor)
    #     return peaks            


    @staticmethod
    def find_peaks(series, threshold=350):
        ekg_values = series["EKG in mV"].values
        peaks = []
        for i in range(1, len(ekg_values) - 1):
            if ekg_values[i] > ekg_values[i - 1] and ekg_values[i] > ekg_values[i + 1] and ekg_values[i] > threshold:
                peaks.append(i)
        peaks_index = pd.Index(peaks, dtype=int)
        series["Peaks"] = np.nan
        series.loc[peaks_index, "Peaks"] = series.loc[peaks_index, "EKG in mV"]

        return series, peaks

    @staticmethod
    def estimate_hr(series, threshold=350):
        # peaks = EKGdata.find_peaks(peaks)
        # result_link = EKGdata.find_peaks(result_link)
        # time = int(len(result_link) / 1000 / 60)
        # heart_rate = len(peaks) / time

        series_with_peaks, peaks = EKGdata.find_peaks(series, threshold)
        series_with_peaks["HeartRate"] = np.nan
        peak_intervals = np.diff(peaks)
        sampling_rate = 1000 
        heart_rates = 60 / (peak_intervals / sampling_rate)
        for i, peak in enumerate(peaks[1:], start=1):
            series_with_peaks.at[peak, "HeartRate"] = heart_rates[i-1]      
        return series_with_peaks

    @staticmethod
    def plot_time_series(self, df):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df["Time in ms"], y=df["EKG in mV"], name="EKG in mV"))
        return fig




if __name__ == "__main__":
    # print("This is a module with some functions to read the EKG data")
    file = open("data/person_db.json")
    person_data = json.load(file)
    ekg_dict = person_data[0]["ekg_tests"][0]
    # print(ekg_dict)
    ekg = EKGdata(ekg_dict)
    print(ekg.df.head())
    # print(EKGdata.load_by_id(1))
    # print(EKGdata.find_peaks(1))

# %% Funktionen