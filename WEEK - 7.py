class AirQuality:

    def __init__(self, city, pm25, pm10):
        self.city = city
        self.pm25 = pm25
        self.pm10 = pm10

    def display(self):
        print(self.city, self.pm25, self.pm10)


a1 = AirQuality("Delhi", 120, 200)
a1.display()