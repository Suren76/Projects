# import math
# import pyowm
import requests
import datetime
# import asyncio
# import logging

LOCATION_ID_ACCUWEATHER = '11586'
API_KEY_ACCUWEATHER = "CFEvIq8sL9Lq6JoJSQvK0XPpjUeYoX66"
LOCATION_KEY_OWM = '614455'
API_KEY_OWM = "3fd60d0b7b747ee2b82669d7cc84b4e0"
LATITUDE = 39.504664648
LONGITUDE = 46.336498654

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

t = "2021-04-14T23:00:00"

print(datetime.datetime.fromisoformat(t))