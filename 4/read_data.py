import csv
import pandas as pd
import numpy as np

def readCSV():
    # Create DataFrame
    # df = pd.read_csv(data, sep =";")
    df = pd.read_csv("3/activities/activity.csv", sep =",")

    duration = df["Duration"]
    Distance = df["Distance"]
    originalPace = df["OriginalPace"]
    heartrate = df["HeartRate"]
    cadence = df["Cadence"]
    powerOriginal = df["PowerOriginal"]
    CalculatedPace = df["CalculatedPace"]
    return df


def getMaxInTime(df, period):
    pb_df = df["PowerOriginal"].rolling(window=period).mean()
    pb = pb_df.max()
    return pb


print(getMaxInTime(readCSV(),5))
