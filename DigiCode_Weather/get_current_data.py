from time import sleep
from datetime import datetime
import json
#from Classes.Weather import OpenWeatherMap, WeatherBit
#from Classes.Sensor import Sensor
#from apis_input_data_connect import *
from main import sensor_dht, wbit, owm


def get_current_data(sensor, weatherbit, openweathermap):
    global current_weather_data_sensor
    global current_weather_data_wbit
    global current_weather_data_owm
    global current_dates

    global temp_sensor
    global humidity_sensor

    global temp_weatherbit
    global humidity_weatherbit

    global temp_openweathermap
    global humidity_openweathermap

    file_for_sensor = open("sensor_data.json", "w+")
    file_for_weatherbit = open("weatherbit_data.json", "w+")
    file_for_openweathermap = open("openweathermap_data.json", "w+")
    current_dates.append(str(datetime.now()))

    humidity, temp = sensor.get_data()
    temp_sensor.append(temp)
    humidity_sensor.append(humidity)
    current_weather_data_sensor = {"date": current_dates, "temp": temp_sensor, "humidity": humidity_sensor}
    json.dump(current_weather_data_sensor, file_for_sensor)

    humidity, temp = weatherbit.get_current_data()
    temp_weatherbit.append(temp)
    humidity_weatherbit.append(humidity)
    current_weather_data_wbit = {"date": current_dates, "temp": temp_weatherbit, "humidity": humidity_weatherbit}
    json.dump(current_weather_data_wbit, file_for_weatherbit)


    humidity, temp = openweathermap.get_current_data()
    temp_openweathermap.append(temp)
    humidity_openweathermap.append(humidity)
    #print(type(current_weather_data_owm))
    current_weather_data_owm = {"date": current_dates, "temp": temp_openweathermap, "humidity": humidity_openweathermap}
    #print(type(current_weather_data_owm))
    json.dump(current_weather_data_owm, file_for_openweathermap)


current_weather_data_sensor = dict()
current_weather_data_wbit = dict()
current_weather_data_owm = dict()

current_dates = list()

temp_sensor = list()
humidity_sensor = list()

temp_weatherbit = list()
humidity_weatherbit = list()

temp_openweathermap = list()
humidity_openweathermap = list()

#wbit = WeatherBit(API_KEY_WEATHERBIT, LATITUDE, LONGITUDE)
#owm = OpenWeatherMap(API_KEY_OWM, LATITUDE, LONGITUDE)
#sensor_dht = Sensor(SENSOR_PIN, SENSOR_MODEl)

while True:
    get_current_data(sensor_dht, wbit, owm)
    print('Save')
    sleep(3600)
