from datetime import datetime

def get_current_data():
    current_weather_data_sensor = list()

    current_dates = list()

    while True:
        file_for_sensor = open(f"sensor_data.json", "w+")
        current_dates.append(str(f"{str(datetime.now())}"))
        current_weather_data_sensor = {"date": current_dates}
        file_for_sensor.write(str(current_weather_data_sensor))
        import time
        time.sleep(10)

get_current_data()