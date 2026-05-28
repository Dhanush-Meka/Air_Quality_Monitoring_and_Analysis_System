# week2_menu.py

records = []

while True:
    print("\n1.Add Record")
    print("2.Display Records")
    print("3.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        city = input("City: ")
        pm25 = input("PM2.5: ")

        records.append([city, pm25])

    elif choice == "2":
        for r in records:
            print(r)

    elif choice == "3":
        break