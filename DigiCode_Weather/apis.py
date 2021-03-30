import requests
# AccuWeather
print(requests.get("http://dataservice.accuweather.com/currentconditions/v1/11586?apikey=ASsOGGnagNRREyX3tFE75igaxQnkPfhL&details=true").json())