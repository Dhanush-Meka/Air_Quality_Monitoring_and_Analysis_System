import json

data = {
    "city": "Delhi",
    "pm25": 120,
    "pm10": 200
}

file = open("air_quality.json", "w")
json.dump(data, file)
file.close()

file = open("air_quality.json", "r")
print(json.load(file))