# from Classes.Weather import OpenWeatherMap, WeatherBit
# from statistic import statistic, summarize_statistic
import sched, time

API_KEY_WEATHERBIT = "49592d44067646cc9392739fa1f8602b"
API_KEY_OWM = "3fd60d0b7b747ee2b82669d7cc84b4e0"
LATITUDE = 39.504664648
LONGITUDE = 46.336498654
SENSOR_PIN = 6
SENSOR_MODEl = 11


def get_weather_current(weatherbit, owm, sensor):
    current_weather = dict()
    current_weather[str(datetime.now().time())[:5]] = {"weatherbit": weatherbit.get_current_data(), "OpenWeatherMap": owm.get_current_data(), "Sensor": sensor.get_data()}
    return current_weather



# s = sched.scheduler(time.time, time.sleep)
# def do_something(sc):
#     s.enter(60, 1, do_something, (sc,))
#
# s.enter(60, 1, do_something, (s,))
# s.run()
#

# #######################################  tests  #################################################################

# wbet = WeatherBit(API_KEY_WEATHERBIT, LATITUDE, LONGITUDE)
# print(wbet.get_current_data())
# print(wbet.get_hourly_data())
# print(wbet.get_daily_data())

# owm = OpenWeatherMap(API_KEY_OWM, LATITUDE, LONGITUDE)
# print(owm.get_current_data())
# print(owm.get_hourly_data())
# print(owm.get_daily_data())

# print(statistic(wbet.get_hourly_data(), owm.get_hourly_data(), "h"))
