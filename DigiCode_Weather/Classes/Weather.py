class WeatherBit:

    requests = __import__("requests")
    datetime = __import__("datetime")

    def __init__(self, API_KEY_WEATHERBIT, LATITUDE, LONGITUDE):
        self.API_KEY_WEATHERBIT = API_KEY_WEATHERBIT
        self.LATITUDE = LATITUDE
        self.LONGITUDE = LONGITUDE

    def get_current_data(self):
        # https://api.weatherbit.io/v2.0/current?lat=39.504664648&lon=46.336498654&key=49592d44067646cc9392739fa1f8602b
        api_weatherbit = self.requests.get(f"https://api.weatherbit.io/v2.0/current?lat={self.LATITUDE}&lon={self.LONGITUDE}&key={self.API_KEY_WEATHERBIT}").json()
        wbit_humidity = api_weatherbit["data"][0]["rh"]
        wbit_Temperature = api_weatherbit["data"][0]["temp"]
        # # print(f"WeatherBit:      humidity {wbit_humidity}   Temperature {wbit_Temperature}")
        return wbit_humidity, wbit_Temperature


    def __get_api_weatherbit_data(self, api_weatherbit_data, t:str):
        date, temp, humidity, weather = list(), list(), list(), list()
        for d in api_weatherbit_data:
            if t == "timestamp_local":
                date.append(str(self.datetime.datetime.fromisoformat(d[t])))
            if t == "datetime":
                date.append(str(d[t]))
            temp.append(d["temp"])
            humidity.append(d["rh"])
            weather.append(d["weather"]["description"])
        return date, temp, humidity, weather


    def get_hourly_data(self):
        api_weatherbit_hourly = self.requests.get(f"https://api.weatherbit.io/v2.0/forecast/hourly?lat={self.LATITUDE}&lon={self.LONGITUDE}&key={self.API_KEY_WEATHERBIT}&hours=48").json()
        api_weatherbit_hourly_data = api_weatherbit_hourly["data"]

        date, temp, humidity, weather = self.__get_api_weatherbit_data(api_weatherbit_hourly_data, "timestamp_local")
        if self.datetime.datetime.now().minute > 10:
            api_weatherbit_hourly_data_filtered = {"date": date[:-1], "temp": temp[:-1], "humidity": humidity[:-1], "weather": weather[:-1]}
        if self.datetime.datetime.now().minute in range(10):
            api_weatherbit_hourly_data_filtered = {"date": date, "temp": temp, "humidity": humidity, "weather": weather}
        # print("WeatherBit - 48 hour", "\n")
        # [[print(f"Hour {i+1}"),print("date :", api_weatherbit_hourly_data_filtered["date"][i]), print("temp :", api_weatherbit_hourly_data_filtered["temp"][i]), print("humidity :", api_weatherbit_hourly_data_filtered["humidity"][i]), print("weather :", api_weatherbit_hourly_data_filtered["weather"][i]),print("\n")] for i in range(len(api_weatherbit_hourly_data_filtered["date"]))]
        return api_weatherbit_hourly_data_filtered

    def get_daily_data(self):
        api_weatherbit_daily: dict = self.requests.get(f"https://api.weatherbit.io/v2.0/forecast/daily?lat={self.LATITUDE}&lon={self.LONGITUDE}&key={self.API_KEY_WEATHERBIT}&days=8").json()
        api_weatherbit_daily_data = api_weatherbit_daily["data"]

        date, temp, humidity, weather = self.__get_api_weatherbit_data(api_weatherbit_daily_data, "datetime")
        api_weatherbit_daily_data_filtered = {"date": date, "temp": temp, "humidity": humidity, "weather": weather}
        # print("WeatherBit - 8 day", "\n")
        # [[print(f"Day {i+1}"),print("date :", api_weatherbit_daily_data_filtered["date"][i]), print("temp :", api_weatherbit_daily_data_filtered["temp"][i]), print("weather :", api_weatherbit_daily_data_filtered["weather"][i]),print("\n")] for i in range(len(api_weatherbit_daily_data_filtered["date"]))]
        return api_weatherbit_daily_data_filtered


class OpenWeatherMap:

    requests = __import__("requests")
    datetime = __import__("datetime")

    def __init__(self, API_KEY_OWM, LATITUDE, LONGITUDE ):
        self.API_KEY_OWM = API_KEY_OWM
        self.LATITUDE = LATITUDE
        self.LONGITUDE = LONGITUDE

    def get_current_data(self):
        api_owm = self.requests.get(f'http://api.openweathermap.org/data/2.5/weather?id=614455&appid={self.API_KEY_OWM}&units=metric').json()
        owm_humidity = api_owm["main"]["humidity"]
        owm_Temperature = api_owm["main"]['temp']
        # print(f"OpenWeatherMap:   humidity {owm_humidity}     Temperature {owm_Temperature}")
        return owm_humidity, owm_Temperature


    def __get_api_owm_data(self, api_owm_data):
        date, temp, humidity, weather = list(), list(), list(), list()
        for d in api_owm_data:

            date.append(str(self.datetime.datetime.fromtimestamp(int(d["dt"]))))
            temp.append(d["temp"])
            humidity.append(d["humidity"])
            weather.append(d["weather"][0]["main"])
        return date, temp, humidity, weather


    def get_hourly_data(self):
        api_owm_hourly = self.requests.get(f'http://api.openweathermap.org/data/2.5/onecall?lat={self.LATITUDE}&lon={self.LONGITUDE}&exclude=alerts,minutely,current,daily&appid={self.API_KEY_OWM}&units=metric').json()
        api_owm_hourly_data = api_owm_hourly["hourly"]

        date, temp, humidity, weather = self.__get_api_owm_data(api_owm_hourly_data)
        if self.datetime.datetime.now().minute > 10:
            api_owm_hourly_data_filtered = {"date": date[1:], "temp": temp[1:], "humidity": humidity[1:], "weather": weather[1:]}
        if self.datetime.datetime.now().minute in range(10):
            api_owm_hourly_data_filtered = {"date": date, "temp": temp, "humidity": humidity, "weather": weather}
        # print("OpenWeatherMap 48 hour", "\n")
        # [[print(f"Hour {i+1}"),print("date :", api_owm_hourly_data_filtered["date"][i]), print("temp :", api_owm_hourly_data_filtered["temp"][i]), print("humidity :", api_owm_hourly_data_filtered["humidity"][i]), print("weather :", api_owm_hourly_data_filtered["weather"][i]),print("\n")] for i in range(len(api_owm_hourly_data_filtered["date"]))]
        return api_owm_hourly_data_filtered

    def get_daily_data(self):
        api_owm_daily: dict = self.requests.get(f'http://api.openweathermap.org/data/2.5/onecall?lat={self.LATITUDE}&lon={self.LONGITUDE}&exclude=alerts,minutely,current,hourly&appid={self.API_KEY_OWM}&units=metric').json()
        api_owm_daily_data = api_owm_daily["daily"]

        date, temp, humidity, weather = self.__get_api_owm_data(api_owm_daily_data)
        api_owm_daily_data_filtered = {"date": [d.split()[0] for d in date], "temp": [t['morn'] for t in temp], "humidity": humidity, "weather": weather}
        # print("OpenWeatherMap - 8 day", "\n")
        # [[print(f"Day {i+1}"),print("date :", api_owm_daily_data_filtered["date"][i]), print("temp :", api_owm_daily_data_filtered["temp"][i]), print("humidity :", api_owm_daily_data_filtered["humidity"][i]), print("weather :", api_owm_daily_data_filtered["weather"][i]),print("\n")] for i in range(len(api_owm_daily_data_filtered["date"]))]
        return api_owm_daily_data_filtered
