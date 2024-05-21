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

def dataAnalysis():
    pass

def createFigure():
    pass

def getMaxInTime(L,period):
    a = 0
    P = 0
    maxAvg = 0
    for i in range(len(L)-period+1):
        for n in range(period):
            a += L[i+n]
            # print(a)
            n += 1
        if a/period > maxAvg:
            maxAvg = a/period
            P = i
            # print("aktueller Maximalwert:",maxAvg,"Zeitraum:",P+1,"-",P+period,"s")
            a = 0
        a = 0
        i += 1
    return maxAvg,P


# df["Time"] = None
print(readCSV()["PowerOriginal"].max())

print(readCSV())