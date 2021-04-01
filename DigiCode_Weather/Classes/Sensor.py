import Adafruit_DHT
from Classes.SensorConnetionError import SensorConnetionError


class Sensor:

    def __init__(self, pin, sensor_model):
        self.__pin = pin
        self.__sensor_model = exec("Adafruit_DHT.DHT" + str(sensor_model))
        # self.sensor_model = getattr(Adafruit_DHT, "DHT"+str(sensor_model))

    def __run(self):
        self.__humidity, self.__temp = Adafruit_DHT.read_retry(self.__sensor_model, self.__pin)
        #try:
        if self.__humidity is None or self.__temp is None:
            print("Fail sensor")
            raise SensorConnetionError("Fail sensor")
        #except SensorConnetionError:
        #    pass

    def get_temp(self):
        self.__run()
        return self.__temp

    def get_humidity(self):
        self.__run()
        return self.__humidity

    def get_data(self):
        self.__run()
        return self.__temp, self.__humidity

    def get_data_live(self):
        while True:
            self.__run()
            print(self.__temp, self.__humidity)