# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Use a breakpoint in the code line below to debug your script.
import requests

API_KEY = "b6907d289e10d714a6e88b30761fae22"
BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid="+ "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"+ "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"


def get_weather_data():
    date = input("Enter the date (YYYY-MM-DD): ")
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        weather_data = response.json()
        for data in weather_data['list']:
            if data['dt_txt'].startswith(date):
                print(f"Temperature on {data['dt_txt']} is {data['main']['temp']}°C")
                break
        else:
            print("No data available for the specified date.")
    else:
        print("Failed to retrieve weather data.")


def get_wind_speed_data():
    date = input("Enter the date (YYYY-MM-DD): ")
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        weather_data = response.json()
        for data in weather_data['list']:
            if data['dt_txt'].startswith(date):
                print(f"Wind Speed on {data['dt_txt']} is {data['wind']['speed']} m/s")
                break
        else:
            print("No data available for the specified date.")
    else:
        print("Failed to retrieve weather data.")


def get_pressure_data():
    date = input("Enter the date (YYYY-MM-DD): ")
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        weather_data = response.json()
        for data in weather_data['list']:
            if data['dt_txt'].startswith(date):
                print(f"Pressure on {data['dt_txt']} is {data['main']['pressure']} hPa")
                break
        else:
            print("No data available for the specified date.")
    else:
        print("Failed to retrieve weather data.")


def main():
    while True:
        print("\nOptions:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            get_weather_data()
        elif choice == '2':
            get_wind_speed_data()
        elif choice == '3':
            get_pressure_data()
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
