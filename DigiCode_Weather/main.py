from Classes.Weather import OpenWeatherMap, WeatherBit
from Classes.Sensor import Sensor
from statistic import statistic, summarize_statistic
from apis_input_data_connect import *
from time import sleep
from datetime import datetime


wbet: WeatherBit = WeatherBit(API_KEY_WEATHERBIT, LATITUDE, LONGITUDE)
owm: OpenWeatherMap = OpenWeatherMap(API_KEY_OWM, LATITUDE, LONGITUDE)
sensor_dht: Sensor = Sensor(SENSOR_PIN, SENDOR_MODEL)


# ## print for home

# #### current
print(wbet.get_current_data())
print(owm.get_current_data())
print(sensor_dht.get_data())

# #### hourly
print(wbet.get_hourly_data())
print(owm.get_hourly_data())

# #### daily
print(wbet.get_daily_data())
print(owm.get_daily_data())

# ## get sensor data and statistic