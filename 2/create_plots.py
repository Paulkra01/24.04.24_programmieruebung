import csv
from matplotlib.pylab import eig
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go


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

def dataAnalysis_max():
    df = readCSV()
    
    power_original_max = df["PowerOriginal"].max()
    #print("Mean PowerOriginal:", power_original_mean)
    #print("Max PowerOriginal:", power_original_max)

    return power_original_max
def dataAnalysis_mean():
    df= readCSV()
    power_original_mean = df["PowerOriginal"].mean()
    power_original_mean = round(power_original_mean, 2)
    return power_original_mean

def createFigure(max_heart_rate):
    df = readCSV()
    
    time = np.arange(len(df))  
    heart_rate = df["HeartRate"]  
    power_original = df["PowerOriginal"]  

    # fig = px.line(df, x=time, y=[power_original, heart_rate])

    # fig.update_traces(line_color='blue', name='Leistung', selector=dict(name='power_original'))
    # fig.update_traces(line_color='red', name='Herzfrequenz', selector=dict(name='heart_rate'))
    # fig.update_layout(yaxis_range=[0, power_original.max()])

    # fig.update_layout(
    #     xaxis_title='Time / s',
    #     yaxis=dict(
    #         title='Power / W',
    #         titlefont=dict(color='blue'),
    #         tickfont=dict(color='blue')
    #     ),
    #     yaxis2=dict(
    #         title='heartrate / bpm',
    #         titlefont=dict(color='red'),
    #         tickfont=dict(color='red'),
    #         overlaying='y',
    #         side='right'
    #     )
    # )

    fig = go.Figure()

    # Hinzufügen der PowerOriginal-Linie
    fig.add_trace(go.Scatter(x=time, y=df['PowerOriginal'], mode='lines', name='Leistung',
                            yaxis='y1'))

    # Hinzufügen der HeartRate-Linie
    fig.add_trace(go.Scatter(x=time, y=df['HeartRate'], mode='lines', name='Herzfrequenz',
                            yaxis='y2'))

    # Layout aktualisieren, um die sekundäre y-Achse zu unterstützen
    fig.update_layout(
        #title='Leistung und Herzfrequenz über die Zeit',
        xaxis_title='Zeit / s',
        yaxis_title='Leistung',
        yaxis2=dict(
            title='Herzfrequenz',
            overlaying='y',
            side='right'
        ),
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        )
    )

# limit power

# max heart rate 
    max_heart_rate_graph = heart_rate.max()
    heart_rate_zones = [0.5 * max_heart_rate, 0.6 * max_heart_rate, 0.7 * max_heart_rate, 0.8 * max_heart_rate, 0.9*max_heart_rate, max_heart_rate]
    color = ['green', 'yellow', 'orange', 'red', 'purple']

# Zonen
    zone_times = []
    for i in range(len(heart_rate_zones)-1):
        zone_time = ((heart_rate >= heart_rate_zones[i]) & (heart_rate < heart_rate_zones[i+1])).sum()
        zone_times.append(zone_time)
        fig.add_shape(type="rect",
                      xref="paper",
                      yref="y2",
                      x0=0,
                      y0=heart_rate_zones[i],
                      x1=1,
                      y1=heart_rate_zones[i+1],
                      fillcolor=color[i],
                      opacity=0.3,
                      layer="below")
    # Erstellen der Legende für die Zonen
    for i, zone_time in enumerate(zone_times):
        fig.add_trace(go.Scatter(x=[None], y=[None], mode='markers', marker=dict(color=color[i]), name=f'Zone {i+1}'))
        # Layout aktualisieren, um die Legende anzuzeigen
        fig.update_layout(showlegend=True, legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))

    # Layout aktualisieren, um die Legende anzuzeigen
    fig.update_layout(showlegend=True)
    
    return fig
        
    
# Zonen Zeit
def power_zonetime():
    df = readCSV()
    power_original = df["PowerOriginal"]
    heart_rate = df["HeartRate"]
    
    max_heart_rate = heart_rate.max()
    heart_rate_zones = [0.5 * max_heart_rate, 0.6 * max_heart_rate, 0.7 * max_heart_rate, 0.8 * max_heart_rate, 0.9*max_heart_rate, max_heart_rate]
    
    # Wieviel in welche zone
    
    zone_avg_power = []
    for i in range(len(heart_rate_zones)-1):
            zone_power = df[(heart_rate >= heart_rate_zones[i]) & (heart_rate < heart_rate_zones[i+1])]['PowerOriginal'].mean()
            zone_power = round(zone_power, 2)
            zone_avg_power.append(str(i+1) + "  =  " + str(zone_power))
    return zone_avg_power    

        
        
  #      zone_avg_power.append(zone_power)
   # return zone_avg_power

def zone_time():
    df = readCSV()
    power_original = df["PowerOriginal"]
    heart_rate = df["HeartRate"]
    
    max_heart_rate = heart_rate.max()
    heart_rate_zones = [0.5 * max_heart_rate, 0.6 * max_heart_rate, 0.7 * max_heart_rate, 0.8 * max_heart_rate, 0.9*max_heart_rate, max_heart_rate]
    avg_zone_time = []
    for i in range(len(heart_rate_zones)-1):
        zone_time = ((heart_rate >= heart_rate_zones[i]) & (heart_rate < heart_rate_zones[i+1])).sum()
        avg_zone_time.append(zone_time)
    return avg_zone_time
    
 #Wieviel in welche zone
    

#Plot anzeigen
    # fig.show()
    




print(dataAnalysis_max())
print(dataAnalysis_mean())