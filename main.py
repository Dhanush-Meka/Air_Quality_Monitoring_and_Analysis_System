import json
import pandas as pd
import matplotlib.pyplot as plt
import os

# AQI calculation
def calculate_aqi(pm25):
    if pm25 <= 50:
        return "Good"
    elif pm25 <= 100:
        return "Moderate"
    elif pm25 <= 200:
        return "Unhealthy"
    else:
        return "Hazardous"

# Add new record
def add_record():
    try:
        pm25 = float(input("Enter PM2.5 value: "))
        pm10 = float(input("Enter PM10 value: "))
        co2 = float(input("Enter CO2 level (ppm): "))
        temp = float(input("Enter Temperature: "))
        hum = float(input("Enter Humidity: "))
    except ValueError:
        print(" Invalid input! Please enter numbers only.")
        return

    record = {
        "PM2.5": pm25,
        "PM10": pm10,
        "CO2": co2,
        "Temperature": temp,
        "Humidity": hum,
        "AQI": calculate_aqi(pm25)
    }

    with open("aqi_data.json", "a") as f:
        f.write(json.dumps(record) + "\n")

    print(" Record added successfully!")

# View records
def view_records():
    if not os.path.exists("aqi_data.json"):
        print("⚠ No data available!")
        return

    print("\n--- Air Quality Records ---")
    with open("aqi_data.json") as f:
        for line in f:
            print(json.loads(line))

# Analyze data
def analyze_data():
    if not os.path.exists("aqi_data.json"):
        print("⚠ No data available!")
        return

    data = []
    with open("aqi_data.json") as f:
        for line in f:
            data.append(json.loads(line))

    if not data:
        print("⚠ No records to analyze!")
        return

    df = pd.DataFrame(data)

    print("\n--- Statistical Analysis ---")
    print(df.describe())

    print("\nAverage PM2.5:", df["PM2.5"].mean())

    # Visualization
    plt.hist(df["PM2.5"], bins=10)
    plt.title("PM2.5 Distribution")
    plt.xlabel("PM2.5 Value")
    plt.ylabel("Frequency")
    plt.grid()
    plt.show()

    # Save CSV (optional)
    df.to_csv("aqi_data.csv", index=False)
    print(" Data also saved as aqi_data.csv")

# Main menu
def main():
    while True:
        print("\n===== AQI Monitoring System =====")
        print("1. Add AQI Record")
        print("2. View Records")
        print("3. Analyze Data")
        print("4. Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Enter a valid number!")
            continue

        if choice == 1:
            add_record()
        elif choice == 2:
            view_records()
        elif choice == 3:
            analyze_data()
        elif choice == 4:
            print("Exiting program...")
            break
        else:
            print(" Invalid choice!")

# Run program
main()