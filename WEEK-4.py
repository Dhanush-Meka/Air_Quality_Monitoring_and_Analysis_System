records = []

def add_record():
    city = input("City: ")
    pm25 = input("PM2.5: ")
    records.append([city, pm25])

def display():
    for r in records:
        print(r)

while True:
    print("1 Add")
    print("2 Display")
    print("3 Exit")

    ch = input()

    if ch == "1":
        add_record()

    elif ch == "2":
        display()

    elif ch == "3":
        break