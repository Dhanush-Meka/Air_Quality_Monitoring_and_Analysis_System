records = []

city = input("City: ")
pm25 = input("PM2.5: ")
pm10 = input("PM10: ")

data = {
    "city": city,
    "pm25": pm25,
    "pm10": pm10
}

records.append(data)

print(records)
