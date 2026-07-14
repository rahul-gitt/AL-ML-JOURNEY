import numpy as np
import pandas as pd

class Lifelens:

    def add_daily_record(self):
        date = input("Enter Date : ")
        sleep = float(input("Sleep Hours : "))
        study = float(input("Study Hours : "))
        coding = float(input("Coding Hours : "))
        screen_time = float(input("Screen Time : "))
        water = float(input("Water Intake : "))
        mood = input("Mood : ")

        userdata = {
            "Date" : date,
            "Sleep": sleep,
            "Study" : study,
            "Coding" : coding,
            "Screen_Time":screen_time,
            "Water":water,
            "Mood": mood
        }
        df = pd.DataFrame([userdata])
        print(df)
        df.to_csv("C:\\Users\\ASUS\\OneDrive\\Desktop\\AL-ML-JOURNEY\\project 1 - LIFELENS\\data\\life_data.csv",
                  index= False,
                  header=False,
                  mode="a"
                  )

    def view_record(self):
        df = pd.read_csv("C:\\Users\\ASUS\\OneDrive\\Desktop\\AL-ML-JOURNEY\\project 1 - LIFELENS\\data\\life_data.csv")
        if df.empty:
            print("No Data found..")

        else:
            print(df.head())
            
    def search_records(self):

        df = pd.read_csv("C:\\Users\\ASUS\\OneDrive\\Desktop\\AL-ML-JOURNEY\\project 1 - LIFELENS\\data\\life_data.csv")

        while True:

            print("\n========== SEARCH ==========")
            print("1. Search by Date")
            print("2. Search by Mood")
            print("3. Exit")

            choice = input("Enter your choice : ")

            if choice == "1":

                search_date = input("Enter Date : ")

                result = df[df["Date"] == search_date]

                if result.empty:
                    print("No Record Found.")
                else:
                    print(result)

            elif choice == "2":

                search_mood = input("Enter Mood : ")

                result = df[df["Mood"] == search_mood]

                if result.empty:
                    print("No Record Found.")
                else:
                    print(result)

            elif choice == "3":
                print("Exiting Search...")
                break

            else:
                print("Invalid Choice.")

    def statistics(self):
        pass

    def filter_data(self):
        pass


user = Lifelens()

while True:

    print("-------------------------------------------")
    print("                 LIFELENS                  ")
    print("-------------------------------------------")
    print("1. Add Daily Record")
    print("2. View Records")
    print("3. Search Records")
    print("4. Statistics")
    print("5. Filter Data")
    print("6. Exit")

    check = int(input("Enter your choice : "))
    if check == 1:
        user.add_daily_record()

    elif check == 2:
        user.view_record()

    elif check == 3:
        user.search_records()

    elif check == 4:
        user.statistics()

    elif check == 5:
        user.filter_data()

    elif check == 6:
        print("Exiting..")
        break

    else :
        print("Invalid input..")