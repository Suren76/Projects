import math

from Classes.SensorConnectionError import SensorConnetionError


class Sensor:

    def __init__(self, pin, sensor_model):
        self.pin = pin
        self.sensor_model = "fild" + sensor_model

    def run(self):
        self.humidity = 2
        self.temperature = self.pin ** 2
        #try:
        if self.humidity is None or self.temperature is None:
            # print("Fail sensor")
            raise SensorConnetionError("Fail sensor")
        #except er.SensorConnetionError as error :
         #   print('SensorConnetionError:', error)
        # print(11111)
        # print(self.pin, self.sensor_model, self.humidity, self.temperature)
        # return self.humidity, self.temperature
    @property
    def pl7p(self):
        print(self.pin, self.sensor_model, self.humidity, self.temperature)


new_sensor = Sensor(5, "1")
new_sensor.run()
#new_sensor.p()

#####################################
def x1():
    print("x1_pass")

def x2():
    print("x2_pass")

#####################################

exec("x"+"1()")
x="l7p"
getattr(new_sensor,"p"+str(x))

m = __import__("math")
print(m.sqrt(49))
import requests
api = requests.get('http://dataservice.accuweather.com/currentconditions/v1/11586?apikey=%09ASsOGGnagNRREyX3tFE75igaxQnkPfhL').json()
humidity = api[0][0][0]
Temperature = api[0][1][0]