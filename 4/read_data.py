import csv
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

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

def getPowerCurve(df,periods):
    best_powers = pd.DataFrame(columns=["BestPower", "Time"])
    
    for index, period in enumerate(periods):
        best_power = getMaxInTime(df, period)
        # Speichert den maximalen Wert im DataFrame
        best_powers.at[index, "BestPower"] = best_power
        best_powers.at[index, "Time"] = period

    return best_powers

# print(getPowerCurve(readCSV(),[1,5,30,60]))


def plotPC(df, best_powers):
    
    fig = px.area(df, x=best_powers["Time"], y=best_powers["BestPower"])
    fig.update_traces(fillcolor="rgba(185, 217, 230, 0.8)", line_color="rgba(93, 157, 181, 0.8)")
    
    fig.add_trace(go.Scatter(x=best_powers["Time"], y=best_powers["BestPower"], name="Watt"))
    # fig.add_trace(go.Scatter(x=best_powers["Time"], y=best_powers["BestPower"], name='Watts'))
    fig.update_layout(hovermode='x unified')
    
    fig.update_layout(
        xaxis_title="Time / s",
        yaxis_title="Power / W"
        # ,xaxis_type="log"
        )
    return fig




if __name__ == '__main__':
    # periods = [1,5,30,60,300,600,1200]
    periods = [i for i in range(1, 1805)]
    df = readCSV()
    best_powers = getPowerCurve(df, periods)
    # print(best_powers.head())
    fig = plotPC(readCSV())
    fig.show()