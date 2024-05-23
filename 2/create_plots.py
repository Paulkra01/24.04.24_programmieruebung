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
    df = readCSV()
    power_original_mean = df["PowerOriginal"].mean()
    power_original_max = df["PowerOriginal"].max()
    #print("Mean PowerOriginal:", power_original_mean)
    #print("Max PowerOriginal:", power_original_max)

    return power_original_mean, power_original_max

def createFigure():
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
    fig.add_trace(go.Scatter(x=time, y=df['PowerOriginal'], mode='lines', name='PowerOriginal',
                            yaxis='y1'))

    # Hinzufügen der HeartRate-Linie
    fig.add_trace(go.Scatter(x=time, y=df['HeartRate'], mode='lines', name='HeartRate',
                            yaxis='y2'))

    # Layout aktualisieren, um die sekundäre y-Achse zu unterstützen
    fig.update_layout(
        title='Power and Heart Rate over Time',
        xaxis_title='Time',
        yaxis_title='PowerOriginal',
        yaxis2=dict(
            title='HeartRate',
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
    max_heart_rate = heart_rate.max()
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
        
    
# Zonen Zeit
    for i, zone_time in enumerate(zone_times):
        zone_power = power_original[(heart_rate >= heart_rate_zones[i]) & (heart_rate < heart_rate_zones[i+1])]
        average_power = zone_power.mean()
        print(f"Average power in zone {i+1}: {average_power}")

    # Wieviel in welche zone
    for i, zone_time in enumerate(zone_times):
        print(f"Time spent in zone {i+1}: {zone_time} seconds")
 #Wieviel in welche zone
    

#Plot anzeigen
    fig.show()




print(createFigure())
print(dataAnalysis())