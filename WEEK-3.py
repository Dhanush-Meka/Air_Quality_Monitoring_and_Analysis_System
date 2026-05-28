# week3_search.py

records = []

for i in range(3):
    city = input("Enter city: ")
    pm25 = input("Enter PM2.5: ")

    records.append([city, pm25])

search = input("Search city: ")

for r in records:
    if r[0].lower() == search.lower():
        print("Record Found:", r)