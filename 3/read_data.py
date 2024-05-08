import csv
import pandas as pd
import numpy as np

def readCSV():
    # Create DataFrame
    # df = pd.read_csv(data, sep =";")
    df = pd.read_csv("activities/activity.csv", sep =",")

    duration = df["Duration"]
    Distance = df["Distance"]
    originalPace = df["OriginalPace"]
    heartrate = df["HeartRate"]
    cadence = df["Cadence"]
    powerOriginal = df["PowerOriginal"]
    CalculatedPace = df["CalculatedPace"]
    return df

def dataAnalysis():
    pass

def createFigure():
    pass


# df["Time"] = None
# df["PowerOriginal"].max()

print(readCSV())