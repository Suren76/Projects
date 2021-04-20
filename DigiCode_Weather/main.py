from Classes.Weather import OpenWeatherMap, WeatherBit
from Classes.Sensor import Sensor
from statistic import statistic, summarize_statistic
from apis_input_data_connect import *
from time import sleep
from datetime import datetime


wbet = WeatherBit(API_KEY_WEATHERBIT, LATITUDE, LONGITUDE)
owm = OpenWeatherMap(API_KEY_OWM, LATITUDE, LONGITUDE)
sensor_dht = Sensor(5, 22)
cd

