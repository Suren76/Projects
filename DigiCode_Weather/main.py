# Ցանկալի է պրոեկտը վերցնել GitHub-ից:
#  https://github.com/Suren76/Projects/tree/main/DigiCode_Weather

#Bug-եր գտնելուց հետո կամ ծրագրային փոփոխությունների դեպքում
#   այն սկզբում թարմացնում եմ GitHub-ում։






from Classes.Weather import OpenWeatherMap, WeatherBit
import json
from Classes.Sensor import Sensor
from statistic import statistic_for_hours, summarize_statistic
from apis_input_data_connect import *
from time import sleep
from datetime import datetime
import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from Styles.Weather_Home import Ui_Home
from Styles.Weather_About import Ui_About
from Styles.Weather_Statistic import Ui_Statistic
from Styles.Weather_SensorLiveMode import Ui_SensorLiveMode
from Styles.Weather_forecast_base import Ui_forecast_base

wbit: WeatherBit = WeatherBit(API_KEY_WEATHERBIT, LATITUDE, LONGITUDE)
owm: OpenWeatherMap = OpenWeatherMap(API_KEY_OWM, LATITUDE, LONGITUDE)
sensor_dht: Sensor = Sensor(SENSOR_PIN, SENSOR_MODEl)
os.system("python get_current_data.py &")

weatherbit_app_start_data = wbit.get_hourly_data()
openweathermap_app_start_data = owm.get_hourly_data()

app = QtWidgets.QApplication(sys.argv)

Home = QtWidgets.QMainWindow()

ui = Ui_Home()
ui.setupUi(Home)
Home.show()

humidity, temp = owm.get_current_data()
ui.OWM_data_temp.setText(str(round(temp)))
ui.OWM_data_humidity.setText(str(round(humidity)))

humidity, temp = wbit.get_current_data()
ui.WeatherBit_data_temp.setText(str(round(temp)))
ui.WeatherBit_data_humidity.setText(str(round(humidity)))

humidity, temp = sensor_dht.get_data()
ui.Sensor_data_temp.setText(str(round(temp)))
ui.Sensor_data_humidity.setText(str(round(humidity)))

ui.timer_for_current_api_data = QTimer()
ui.timer_for_current_sensor_data = QTimer()

def send_current_api_data():
    humidity, temp = owm.get_current_data()
    ui.OWM_data_temp.setText(str(round(temp)))
    ui.OWM_data_humidity.setText(str(round(humidity)))

    humidity, temp = wbit.get_current_data()
    ui.WeatherBit_data_temp.setText(str(round(temp)))
    ui.WeatherBit_data_humidity.setText(str(round(humidity)))

def send_current_sensor_data():
    humidity, temp = sensor_dht.get_data()
    ui.Sensor_data_temp.setText(str(round(temp)))
    ui.Sensor_data_humidity.setText(str(round(humidity)))



ui.timer_for_current_api_data.timeout.connect(send_current_api_data)
ui.timer_for_current_api_data.start(3600000)

ui.timer_for_current_sensor_data.timeout.connect(send_current_sensor_data)
ui.timer_for_current_sensor_data.start(60000)


def open_About_window():
    global About
    About = QtWidgets.QMainWindow()
    ui = Ui_About()
    ui.setupUi(About)
    About.show()


def open_Sensor_Live_Mode_window():
    global Sensor_Live_Mode
    Sensor_Live_Mode = QtWidgets.QMainWindow()
    ui = Ui_SensorLiveMode()
    ui.setupUi(Sensor_Live_Mode)
    Sensor_Live_Mode.show()
    ui.timer_for_live_mode_sensor_data = QTimer()

    def send_live_mode_sensor_data():
        humidity, temp = sensor_dht.get_data()
        ui.Sensor_data_temp.setText(str(int(temp)))
        #ui.Sensor_data_temp.setText(str(datetime.now().second))
        ui.Sensor_data_humidity.setText(str(int(humidity)))

    ui.timer_for_live_mode_sensor_data.timeout.connect(send_live_mode_sensor_data)
    ui.timer_for_live_mode_sensor_data.start(700)


def open_Weather_for_Week_window():

    global Weather_for_Week
    Weather_for_Week = QtWidgets.QMainWindow()
    ui = Ui_forecast_base("Weather for Week")
    ui.setupUi(Weather_for_Week)
    Weather_for_Week.show()

    wbit_data = wbit.get_daily_data()
    owm_data = owm.get_daily_data()
    for i in range(len(owm_data["date"])-1):
        ui.frame_base_owm(round(owm_data["temp"][i]), owm_data["weather"][i], round(owm_data["humidity"][i]), owm_data["date"][i])
        ui.frame_base_wbit(round(wbit_data["temp"][i]), wbit_data["weather"][i], round(wbit_data["humidity"][i]), wbit_data["date"][i])


def open_Hourly_Weather_window():
    global Hourly_Weather
    Hourly_Weather = QtWidgets.QMainWindow()
    ui = Ui_forecast_base("Hourly Weather")
    ui.setupUi(Hourly_Weather)
    Hourly_Weather.show()

    wbit_data = wbit.get_hourly_data()
    owm_data = owm.get_hourly_data()
    for i in range(len(owm_data["date"])-1):
        ui.frame_base_owm(round(owm_data["temp"][i]), owm_data["weather"][i], round(owm_data["humidity"][i]), owm_data["date"][i])
        ui.frame_base_wbit(round(wbit_data["temp"][i]), wbit_data["weather"][i], round(wbit_data["humidity"][i]), wbit_data["date"][i])


def open_Statistic_window():
    global Statistic
    Statistic = QtWidgets.QMainWindow()
    ui = Ui_Statistic()
    ui.setupUi(Statistic)
    Statistic.show()

    sensor_get_data = json.load(open("sensor_data.json"))
    weatherbit_get_data = json.load(open("weatherbit_data.json"))
    openweathermap_get_data = json.load(open("openweathermap_data.json"))

    for i in range(len(sensor_get_data["date"])):
        i = i-1
        ui.SensorData_base(sensor_get_data['temp'][i], sensor_get_data['humidity'][i], sensor_get_data['date'][i])

        wbit_statistic_current_data = statistic_for_hours(sensor_get_data, weatherbit_app_start_data)
        owm_statistic_current_data = statistic_for_hours(sensor_get_data, openweathermap_app_start_data)

        wbit_statistic_get_data = statistic_for_hours(sensor_get_data, weatherbit_get_data)
        owm_statistic_get_data = statistic_for_hours(sensor_get_data, openweathermap_get_data)

        sum_st_wbit_current = summarize_statistic(wbit_statistic_current_data)
        sum_st_owm_current = summarize_statistic(owm_statistic_current_data)

        sum_st_wbit_get = summarize_statistic(wbit_statistic_get_data)
        sum_st_owm_get = summarize_statistic(owm_statistic_get_data)

    for date_current_get in wbit_statistic_current_data:
        ui.cds_owm_frame_base(owm_statistic_current_data[date_current_get]['temp'], owm_statistic_current_data[date_current_get]['humidity'], date_current_get)
        ui.cds_wbit_frame_base(wbit_statistic_current_data[date_current_get]['temp'], wbit_statistic_current_data[date_current_get]['humidity'], date_current_get)
    ui.cds_wbit_frame_base(sum_st_wbit_current["temp"], sum_st_wbit_current["humidity"],"Sum stasistic date")
    ui.cds_owm_frame_base(sum_st_owm_current["temp"], sum_st_owm_current["humidity"],"Sum stasistic date")
    for date_get in wbit_statistic_get_data:
        ui.frame_OWM_sdds_base(owm_statistic_get_data[date_get]['temp'], owm_statistic_get_data[date_get]['humidity'], date_get)
        ui.frame_WeatherBit_sdds_base(wbit_statistic_get_data[date_get]['temp'], wbit_statistic_get_data[date_get]['humidity'], date_get)
    ui.frame_WeatherBit_sdds_base(sum_st_wbit_get["temp"], sum_st_wbit_get["humidity"],"Sum stasistic date")
    ui.frame_OWM_sdds_base(sum_st_owm_get["temp"], sum_st_owm_get["humidity"],"Sum stasistic date")

# clicked
ui.About.clicked.connect(open_About_window)
ui.actionSensor_Live_Mode.triggered.connect(open_Sensor_Live_Mode_window)
ui.actionWeather_for_Week.triggered.connect(open_Weather_for_Week_window)
ui.actionHourly_Weather.triggered.connect(open_Hourly_Weather_window)
ui.actionStatistic.triggered.connect(open_Statistic_window)

sys.exit(app.exec_())
