class Record:
    def display(self):
        print("Air Quality Record")


class AirQuality(Record):


    def __init__(self, city, pm25):
        self.city = city
        self.pm25 = pm25

    def display(self):
        print("City:", self.city)
        print("PM2.5:", self.pm25)


a = AirQuality("Hyderabad", 90)
a.display()