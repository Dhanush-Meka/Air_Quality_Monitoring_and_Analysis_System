import pandas as pd

data = {
    "City": ["Delhi", "Mumbai", "Hyderabad"],
    "PM25": [120, 80, 70]
}

df = pd.DataFrame(data)

print(df)

print("Average Pollution:", df["PM25"].mean())
