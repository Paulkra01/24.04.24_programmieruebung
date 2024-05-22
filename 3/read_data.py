import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



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

    # Plot
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

# über die Zeit
    ax1.plot(time, power_original, color="blue", label="Leistung")
    ax1.set_ylabel("Leistung")
    ax1.set_xlabel("Zeit")

# heartrate über die zeit
    ax2.plot(time, heart_rate, color="red", label="Herzfrequenz")
    ax2.set_ylabel("Herzfrequenz in Sekunden")

   
   

# limit power
    ax1.set_ylim([0, power_original.max()])
# max heart rate 
    max_heart_rate = heart_rate.max()
    heart_rate_zones = [0.5 * max_heart_rate, 0.6 * max_heart_rate, 0.7 * max_heart_rate, 0.8 * max_heart_rate, 0.9*max_heart_rate, max_heart_rate]
    color = ['green', 'yellow', 'orange', 'red', 'purple']

# Zonen
    zone_times = []
    for i in range(len(heart_rate_zones)-1):
        zone_time = ((heart_rate >= heart_rate_zones[i]) & (heart_rate < heart_rate_zones[i+1])).sum()
        zone_times.append(zone_time)
        ax2.fill_between(time, heart_rate_zones[i], heart_rate_zones[i+1], alpha=0.3)
    
# Zonen Zeit
    for i, zone_time in enumerate(zone_times):
        zone_power = power_original[(heart_rate >= heart_rate_zones[i]) & (heart_rate < heart_rate_zones[i+1])]
        average_power = zone_power.mean()
        print(f"Average power in zone {i+1}: {average_power}")
 #Wieviel in welche zone
    

#Plot anzeigen
    plt.show()
print(createFigure())