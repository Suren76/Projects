from Classes.Weather import OpenWeatherMap, WeatherBit

API_KEY_WEATHERBIT = "49592d44067646cc9392739fa1f8602b"
API_KEY_OWM = "3fd60d0b7b747ee2b82669d7cc84b4e0"
LATITUDE = 39.504664648
LONGITUDE = 46.336498654


# #######################################  test  #################################################################

wbet = WeatherBit(API_KEY_WEATHERBIT, LATITUDE, LONGITUDE)
wbet.get_current_data()
wbet.get_hourly_data()
wbet.get_daily_data()

owm = OpenWeatherMap(API_KEY_OWM, LATITUDE, LONGITUDE)
owm.get_current_data()
owm.get_hourly_data()
owm.get_daily_data()
