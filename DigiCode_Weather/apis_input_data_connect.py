import requests
import datetime

LOCATION_KEY_ACCUWEATHER = '11586'
API_KEY_ACCUWEATHER = "CFEvIq8sL9Lq6JoJSQvK0XPpjUeYoX66"
LOCATION_KEY_OWM = '614455'
API_KEY_OWM = "3fd60d0b7b747ee2b82669d7cc84b4e0"
LATITUDE = 39.504664648
LONGITUDE = 46.336498654

def get_api_owm_data(api_owm_data):
    date, temp, humidity, weather = list(), list(), list(), list()
    for d in api_owm_data:
        date.append(str(datetime.datetime.fromtimestamp(int(d["dt"]))))
        temp.append(d["temp"])
        humidity.append(d["humidity"])
        weather.append(d["weather"][0]["main"])
    return date, temp, humidity, weather

########################################  current  #################################################################
# AccuWeather
api_accuweather = requests.get(f"http://dataservice.accuweather.com/currentconditions/v1/{LOCATION_KEY_ACCUWEATHER}?apikey={API_KEY_ACCUWEATHER}&details=true").json()
accuw_humidity = api_accuweather[0]["RelativeHumidity"]
accuw_Temperature = api_accuweather[0]["Temperature"]["Metric"]["Value"]

# OpenWeatherMap api.openweathermap.org/data/2.5/weather?id={city id}&appid={API key}
api_owm = requests.get(f'http://api.openweathermap.org/data/2.5/weather?id={LOCATION_KEY_OWM}&appid={API_KEY_OWM}&units=metric').json()
owm_humidity = api_owm["main"]["humidity"]
owm_Temperature = api_owm["main"]['temp']

# data
print(f"AccuWeather:      humidity {accuw_humidity}   Temperature {accuw_Temperature}")
print(f"OpenWeatherMap:   humidity {owm_humidity}     Temperature {owm_Temperature}")
print("\n"*3)

# ########################################  hourly  #################################################################
# OpenWeatherMap

api_owm_hourly = requests.get(f'http://api.openweathermap.org/data/2.5/onecall?lat={LATITUDE}&lon={LONGITUDE}&exclude=alerts,minutely,current,daily&appid={API_KEY_OWM}&units=metric').json()
api_owm_hourly_data = api_owm_hourly["hourly"]

date, temp, humidity, weather = get_api_owm_data(api_owm_hourly_data)
api_owm_hourly_data_filtered = {"date": date, "temp": temp, "humidity": humidity, "weather": weather}
[[print(f"Hour {i+1}"),print("date :", api_owm_hourly_data_filtered["date"][i]), print("temp :", api_owm_hourly_data_filtered["temp"][i]), print("humidity :", api_owm_hourly_data_filtered["humidity"][i]), print("weather :", api_owm_hourly_data_filtered["weather"][i]),print("\n")] for i in range(len(api_owm_hourly_data_filtered["date"]))]


# ########################################  daily  #################################################################
# OpenWeatherMap
api_owm_daily: dict = requests.get(f'http://api.openweathermap.org/data/2.5/onecall?lat={LATITUDE}&lon={LONGITUDE}&exclude=alerts,minutely,current,hourly&appid={API_KEY_OWM}&units=metric').json()
api_owm_daily_data = api_owm_daily["daily"]

date, temp, humidity, weather = get_api_owm_data(api_owm_daily_data)
api_owm_daily_data_filtered = {"date": date, "temp": temp, "humidity": humidity, "weather": weather}

[[print(f"Day {i+1}"),print("date :", api_owm_daily_data_filtered["date"][i]), print("temp :", api_owm_daily_data_filtered["temp"][i]), print("humidity :", api_owm_daily_data_filtered["humidity"][i]), print("weather :", api_owm_daily_data_filtered["weather"][i]),print("\n")] for i in range(len(api_owm_daily_data_filtered["date"]))]