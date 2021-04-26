from time import sleep
from datetime import datetime


def get_current_data(sensor, weatherbit, openweathermap):
    current_weather_data_sensor = list()
    current_weather_data_wbit = list()
    current_weather_data_owm = list()
    current_dates = list()

    temp_sensor = list()
    humidity_sensor = list()

    temp_weatherbit = list()
    humidity_weatherbit = list()

    temp_openweathermap = list()
    humidity_openweathermap = list()

    while True:
        file_for_sensor = open(f"sensor_data.json", "w+")
        file_for_weatherbit = open(f"weatherbit_data.json", "w+")
        file_for_openweathermap = open(f"openweathermap_data.json", "w+")
        current_dates.append(str(f"{str(datetime.now())}"))

        humidity, temp = sensor.get_data()
        temp_sensor.append(humidity)
        humidity_sensor.append(temp)
        current_weather_data_sensor = {"date": current_dates, "temp": temp_sensor, "humidity": humidity_sensor}
        file_for_sensor.writelines(str(current_weather_data_sensor))

        humidity, temp = weatherbit.get_current_data()
        temp_weatherbit.append(humidity)
        humidity_weatherbit.append(temp)
        current_weather_data_wbit = {"date": current_dates, "temp": temp_weatherbit, "humidity": humidity_weatherbit}
        file_for_weatherbit.writelines(str(current_weather_data_wbit))

        humidity, temp = openweathermap.get_current_data()
        temp_openweathermap.append(humidity)
        humidity_openweathermap.append(temp)
        current_weather_data_owm = {"date": current_dates, "temp": temp_openweathermap, "humidity": humidity_openweathermap}
        file_for_openweathermap.writelines(str(current_weather_data_owm))
        sleep(3600)

if __name__ == "__main__":
     print(get_current_data())


# get_sensor_current_data()