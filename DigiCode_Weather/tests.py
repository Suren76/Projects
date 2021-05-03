# import math
# import pyowm
# import requests.packages.urllib3.request
# import datetime
# import time
# import asyncio
# import logging
# import sched
# from get_current_data import get_sensor_current_data


from Classes.Weather import OpenWeatherMap, WeatherBit
#from Classes.Sensor import Sensor
# from statistic import statistic_for_hours, summarize_statistic
from apis_input_data_connect import *
# from time import sleep
from datetime import datetime
# from multiprocessing import Process
# import sys
import os
import platform


wbet: WeatherBit = WeatherBit(API_KEY_WEATHERBIT, LATITUDE, LONGITUDE)
owm: OpenWeatherMap = OpenWeatherMap(API_KEY_OWM, LATITUDE, LONGITUDE)
# sensor_dht: Sensor = Sensor(SENSOR_PIN, SENSOR_MODEl)


# from accuweather import (
#     AccuWeather,
#     ApiError,
#     InvalidApiKeyError,
#     InvalidCoordinatesError,
#     RequestsExceededError,
# )
#
# from aiohttp import ClientError, ClientSession
#
# LOCATION_KEY = '11586'
# API_KEY = "ASsOGGnagNRREyX3tFE75igaxQnkPfhL"
# LATITUDE = 39.504664648
# LONGITUDE = 46.336498654
# AccuWeather(API_KEY, ClientSession(),
#             )
# async def main():
#     async with ClientSession() as websession:
#         accuweather = AccuWeather(
#             API_KEY, websession, latitude=LATITUDE, longitude=LONGITUDE
#         )
#         current_conditions = await accuweather.async_get_current_conditions()
#         forecast = await accuweather.async_get_forecast(metric=True)
#
#         print(f"Location: {accuweather.location_name} ({accuweather.location_key})")
#         print(f"Requests remaining: {accuweather.requests_remaining}")
#         print(f"Current: {current_conditions}")
#         print(f"Forecast: {forecast}")
#
#
# print("AccuWeather")

# loop = asyncio.get_event_loop().run_until_complete(main())
#
#
# key_1 = "1e1e7710151b15253c1e16aa2ee79792"
# owm = pyowm.OWM(api_key=key_1)
# w = owm.weather_manager().weather_at_id(614455).weather
#
# print("OpenWeatherMap")
# print(w.temperature('celsius'), w.humidity)
# api_owm_hourly: dict = requests.get(f'http://api.openweathermap.org/data/2.5/onecall?lat={LATITUDE}&lon={LONGITUDE}&exclude=alerts,minutely,current,daily&appid={API_KEY_OWM}&units=metric').json()
# api_owm_hourly_data = api_owm_hourly["hourly"]

# def get_api_owm_data(api_owm_data):
#     date, temp, humidity, weather = list(), list(), list(), list()
#     for d in api_owm_data:
#         date.append(str(datetime.datetime.fromtimestamp(int(d["dt"]))))
#         temp.append(d["temp"])
#         humidity.append(d["humidity"])
#         weather.append(d["weather"][0]["main"])
#     return date, temp, humidity, weather
# date, temp, humidity, weather = get_api_owm_data(api_owm_hourly_data)
# api_owm_hourly_data_filtered = {"date": date, "temp": temp, "humidity": humidity, "weather": weather}
# [[print(f"Hour {i+1}"),print("date :", api_owm_hourly_data_filtered["date"][i]), print("temp :", api_owm_hourly_data_filtered["temp"][i]), print("humidity :", api_owm_hourly_data_filtered["humidity"][i]), print("weather :", api_owm_hourly_data_filtered["weather"][i]),print("\n")] for i in range(len(api_owm_hourly_data_filtered["date"]))]
# api_accuweather_daily: dict = requests.get(f"http://dataservice.accuweather.com/forecasts/v1/daily/5day/115{LOCATION_ID_ACCUWEATHER}ikey={API_KEY_ACCUWEATHER}&details=true&metric=true").json()
# api_accuweather_daily_data = api_accuweather_daily["DailyForecasts"][0]
#
# temp = api_accuweather_daily_data["Temperature"]
# date = api_accuweather_daily["Date"]
# weather = api_accuweather_data["Day"]["PrecipitationType"]

# t = "2021-04-17 02:00:00"
#
# print(t.split()[0].split("-")[2])
#
# import Classes.SensorConnectionError as ggg
#
# if t.split()[0].split("-")[2] != 5:
#     raise ggg

# def d(n):
#         num = int(input())
#         num += 1
#         yield num
#
#
# while True:
#    print(next(d(1)))
# s = sched.scheduler(time.time, time.sleep)
#
# s.enter(4, 1, print(4), s)
# s.run()

# def get_weather_current(weatherbit, owm): # , sensor):
#     current_weather = dict()
#     current_weather[str(datetime.now().time())[:5]] = {"weatherbit": weatherbit.get_current_data(), "OpenWeatherMap": owm.get_current_data()} # , "Sensor": sensor.get_data()}
#     return current_weather

# l = list()
# l1 = 5
# def f1():
#     global l1
#     l1 += 1
#     sleep(2)
#     print(l1,"fnc")

# print(1)



# s = sched.scheduler(time.time, time.sleep)
# def do_something(sc):
#     s.enter(60, 1, do_something, (sc,))
#
# s.enter(60, 1, do_something, (s,))
# s.run()
#


# def myFunc():
#     f = open('file.txt', 'r+')
#     while True:
#         print(len(f))
#         f.write(str(datetime.now()))
#         sleep(2)

# import os, asyncio

# async def tail(f, queue):
#     f.seek(0, os.SEEK_END)
#     while True:
#         line = f.readline()
#         if not line:
#             await asyncio.sleep(0.1)
#             continue
#         await queue.put(line)

# async def consume(queue):
#     lines = []
#     while True:
#         next_line = await queue.get()
#         lines.append(next_line)
#         # it is not clear if you want somefun to receive the next
#         # line or *all* lines, but it's easy to do either
#         somefun(next_line)

# def somefun(line):
#     # do something with line
#     print(f'line: {line!r}')

# async def main():
#     queue = asyncio.Queue()
#     with open('file.txt') as f:
#         await asyncio.gather(tail(f, queue), consume(queue))

# if __name__ == '__main__':
#     asyncio.run(main())
#     # or, on Python older than 3.7:
#     #asyncio.get_event_loop().run_until_complete(main())
#         global current_weather_data_sensor
# current_weather_data_sensor = dict()



#current_weather_data_sensor = list()
#file_to_save = open("sensor_data.txt", "w+")

#while True:
#    current_weather_data_sensor.append(str(datetime.now().time()))
#    file_to_save.write(str(current_weather_data_sensor))
#    print(current_weather_data_sensor)
#    sleep(10)


# def get_sensor_current_data():
#     current_weather_data_sensor = list()
#     while True:
#         f = file_to_save = open("sensor_data.txt", "w+")
#         current_weather_data_sensor.append(str(datetime.now().time()))
#         f.writelines(str(current_weather_data_sensor))
#         print(current_weather_data_sensor)
#         # yield current_weather_data_sensor
#         sleep(10)

# if __name__ == "__main__":

#     print(get_sensor_current_data())
# do = input()
# if do == "1":
#     if platform.system() == "Windows":
#         os.system("start /min  cmd /k python test_current_data_save.py")
#     if platform.system() == "Linux":
#         os.system("python get_current_data.py &")
#     # get_sensor_current_data()
#     while True:
#         f = input("0 - print data"
#                   "\nq - quit\n")
#         if f == "0":
#             fl = open("sensor_data.json", "r+")
#             print(fl.read())
#         if f == "q":
#             break

# b = {"data":datetime.month(), "time":datetime.now().time()}
# , {"data": str(datetime.month()), "time": str(datetime.now().time())}]
# l = list()
# l.append(open("sensor_data.json", "r+").read())
import time
import json
# print((type(open("sensor_data.json", "r+").read())))

# with open('sensor_data.json') as json_file:
#     data = json.load(json_file)
#     print(data, type(data))

f = json.load(open("sensor_data.json"))
#print(f, type(f))
print(wbet.get_hourly_data())
#print(owm.get_hourly_data())
# while True:
#     print(sensor_dht.get_data())