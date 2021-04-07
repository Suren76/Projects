import requests
import pyowm
import accuweather


# AccuWeather
api_accuweather = requests.get('http://dataservice.accuweather.com/currentconditions/v1/11586?apikey=%09ASsOGGnagNRREyX3tFE75igaxQnkPfhL&details=true').json()
accuw_humidity = api_accuweather[0]["RelativeHumidity"]
accuw_Temperature = api_accuweather[0]["Temperature"]["Metric"]["Value"]
accu = accuweather.AccuWeather(api_key="09ASsOGGnagNRREyX3tFE75igaxQnkPfhL", location_key="11586")
aw = accu.async_get_current_conditions()
print(aw,"\n"*3)
# OpenWeatherMap
api_owm = requests.get('http://api.openweathermap.org/data/2.5/weather?id=614455&appid=1e1e7710151b15253c1e16aa2ee79792&units=metric').json()
owm_humidity = api_owm["main"]["humidity"]
owm_Temperature = api_owm["main"]['temp']
key_1 = "1e1e7710151b15253c1e16aa2ee79792"
owm = pyowm.OWM(api_key=key_1)
w = owm.weather_manager().weather_at_id(614455).weather

print(w, '\n', w.temperature('celsius'), w.humidity)

# data
# print(f"AccuWeather:      humidity {accuw_humidity}   Temperature {accuw_Temperature}")
# print(f"OpenWeatherMap:   humidity {owm_humidity}     Temperature {owm_Temperature}")
