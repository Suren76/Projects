from datetime import datetime
import json
from time import sleep


def get_current_data():

    global current_dates
    file_for_sensor = open(f"sensor_data.json", "w+")
    current_dates.append(str(f"{str(datetime.now())}"))
    current_weather_data_sensor = {"date": current_dates}
    json.dump(current_weather_data_sensor, file_for_sensor)


current_dates = list()

while True:
    get_current_data()
    sleep(10)


