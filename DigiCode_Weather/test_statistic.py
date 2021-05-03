from Classes.Weather import OpenWeatherMap, WeatherBit
import json
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

app = QtWidgets.QApplication(sys.argv)

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

        wbit_statistic_current_data = statistic_for_hours(sensor_get_data, wbit.get_hourly_data())
        owm_statistic_current_data = statistic_for_hours(sensor_get_data, owm.get_hourly_data())

        wbit_statistic_get_data = statistic_for_hours(sensor_get_data, weatherbit_get_data)
        owm_statistic_get_data = statistic_for_hours(sensor_get_data, openweathermap_get_data)

        sum_st_wbit_current = summarize_statistic(wbit_statistic_current_data)
        sum_st_owm_current = summarize_statistic(owm_statistic_current_data)

        sum_st_wbit_get = summarize_statistic(wbit_statistic_get_data)
        sum_st_owm_get = summarize_statistic(owm_statistic_get_data)

    for date_current_get in wbit_statistic_current_data:
        ui.cds_owm_frame_base(owm_statistic_current_data[date_current_get]['temp'], owm_statistic_current_data[date_current_get]['humidity'], str(date_current_get))
        ui.cds_wbit_frame_base(wbit_statistic_current_data[date_current_get]['temp'], wbit_statistic_current_data[date_current_get]['humidity'], str(date_current_get))
    ui.cds_wbit_frame_base(sum_st_wbit_current["temp"], sum_st_wbit_current["humidity"],"Sum stasistic date")
    ui.cds_owm_frame_base(sum_st_owm_current["temp"], sum_st_owm_current["humidity"],"Sum stasistic date")

    for date_get in wbit_statistic_get_data:
        ui.frame_OWM_sdds_base(owm_statistic_get_data[date_get]['temp'], owm_statistic_get_data[date_get]['humidity'], date_get)
        ui.frame_WeatherBit_sdds_base(wbit_statistic_get_data[date_get]['temp'], wbit_statistic_get_data[date_get]['humidity'], date_get)
    ui.frame_WeatherBit_sdds_base(sum_st_wbit_get["temp"], sum_st_wbit_get["humidity"],"Sum stasistic date")
    ui.frame_OWM_sdds_base(sum_st_owm_get["temp"], sum_st_owm_get["humidity"],"Sum stasistic date")


open_Statistic_window()

sys.exit(app.exec_())
