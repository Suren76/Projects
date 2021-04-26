# Ցանկալի է պրոեկտը վերցնել GitHub-ից:
#  https://github.com/Suren76/Projects/tree/main/DigiCode_Weather

#Bug-եր գտնելուց հետո կամ ծրագրային փոփոխությունների դեպքում
#   այն սկզբում թարմացնում եմ GitHub-ում։






from Classes.Weather import OpenWeatherMap, WeatherBit
from Classes.Sensor import Sensor
from statistic import statistic_for_hours, statistic_for_days, summarize_statistic
from apis_input_data_connect import *
from time import sleep
from datetime import datetime
import os


wbet: WeatherBit = WeatherBit(API_KEY_WEATHERBIT, LATITUDE, LONGITUDE)
owm: OpenWeatherMap = OpenWeatherMap(API_KEY_OWM, LATITUDE, LONGITUDE)
sensor_dht: Sensor = Sensor(SENSOR_PIN, SENSOR_MODEl)
os.system("python get_current_data.py &")

# ## print for home
do = input("1: Current data"
           "\n2: Hourly data"
           "\n3: Daily data"
           "\n4: Statistic"
           " ")
# #### current
if do == "1":
    print(wbet.get_current_data())
    print(owm.get_current_data())
    print(sensor_dht.get_data())

# #### hourly
if do == "2":
    print(wbet.get_hourly_data())
    print(owm.get_hourly_data())

# #### daily
if do == "3":
    print(wbet.get_daily_data())
    print(owm.get_daily_data())

# ## get sensor data and statistic
if do == "4":
    print(statistic_for_hours(open("sensor_data.json", "r+").read(), wbet.get_hourly_data()))
    print(statistic_for_hours(open("sensor_data.json", "r+").read(), owm.get_hourly_data()))
