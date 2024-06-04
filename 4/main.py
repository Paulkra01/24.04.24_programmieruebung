import read_data as rd

if __name__ == '__main__':
    filepath = "3/activities/activity.csv"  # Update with the correct path to your CSV file
    periods = [i for i in range(1, 1805)]  # Example periods from 1 to 1804 seconds
    
    df = rd.readCSV()
    
    if df is not None:
        best_powers = rd.getPowerCurve(df, periods)
        fig = rd.plotPC(df, best_powers)
        fig.show()
    else:
        print("Failed to read the CSV file.")
