import matplotlib.pyplot as plt

cities = ["Delhi", "Mumbai", "Hyderabad"]
pm25 = [120, 80, 70]

plt.bar(cities, pm25)

plt.title("Air Pollution Levels")
plt.xlabel("City")
plt.ylabel("PM2.5")

plt.show()